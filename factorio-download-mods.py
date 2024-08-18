import json
import os
import requests
from bs4 import BeautifulSoup
from rich.default_styles import DEFAULT_STYLES
from rich.style import Style

# The only way to change styles of some columns without modifying (within) the library
DEFAULT_STYLES["progress.download"] = Style(color="cyan3")
DEFAULT_STYLES["progress.data.speed"] = Style(color="pink3")

# This package uses "DEFAULT_STYLES" so have to import it after the changes
from rich.progress import BarColumn, DownloadColumn, Progress, TextColumn, TransferSpeedColumn # type: ignore # noqa: E402


class Downloader:
    """Downloads given mods listed in a file from mods.factorio.com

    Args:
        path (str): A path to the file with listed mods (one mod on one line, no new line at the end)
        gameVersion (float): A version of the game (1.1, 1.0, 0.18, 0.17, etc.)
    """

    _progressBarColumns= [
        TextColumn("[cyan][progress.description]{task.description}"),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn()
    ]

    def __init__(self, path: str, gameVersion: float) -> None:
        with open(f"{os.getenv('APPDATA')}\\Factorio\\player-data.json", "r", encoding="utf-8") as f:
            playerDataJson = json.load(f) # Get player's token and username
            self._data = dict()
            self._data["username"] = playerDataJson["service-username"]
            self._data["token"] = playerDataJson["service-token"]
            self._data["version"] = gameVersion
            self._data["modsFile"] = path

    def execute(self) -> None:
        """Find and download the mods"""
        mods = self._fetch(self._find())
        print("Downloading...")
        for mod in mods:
            self._download(mod)
        print("Done")

    # FIXME: Some mods can already be found by API, so it would be better to do that first
    # to cut down search count on the webpage since it takes quite a while to get
    # a response from the request this way
    def _find(self) -> list[str]:
        """Get mods ids from a first result on the search webpage"""
        notFound = []
        ids = []
        with open(self._data["modsFile"], "r") as f:
            names = f.read().splitlines()
            for i, name in enumerate(names, start=1):
                print('Searching the mods... ', f"{i}/{len(names)}", sep='', end='\r', flush=True)
                params = {"query": name, "exclude_category": "internal", "factorio_version": str(self._data["version"]), "sort_attribute": "relevancy"}
                response = requests.get("https://mods.factorio.com/search", params)
                soup = BeautifulSoup(response.text, 'lxml')
                match = soup.find("a", class_="result-field", href=True)
                if match is None:
                    notFound.append(name)
                else:
                    ids.append(match["href"].split("/mod/")[1].split("?")[0]) # type: ignore
            print()

        if len(notFound):
            print(f"Didn't found these mods: {notFound}")

        return ids

    def _fetch(self, ids: list[str]) -> list[dict]:
        """Get mods info from the official API (https://wiki.factorio.com/Mod_portal_API)"""
        mods = []
        i = 0
        targetAmount = len(ids)

        # Using while loop since maximum mods retrieved per request is 25
        while len(ids) > 0:
            print('Getting download urls... ', f"{i}/{targetAmount}", sep='', end='\r', flush=True)
            response = requests.get("https://mods.factorio.com/api/mods", {"page_max": "max", "version": str(self._data["version"]), "namelist": ','.join(ids)}) # Comma-separated names just make the request url shorter
            if response.status_code == 200:
                results = response.json()["results"]
                for result in results:
                    for release in result["releases"]:
                        if float(release["info_json"]["factorio_version"]) == self._data["version"]:
                            mods.append({"file_name": release["file_name"], "download_url": release["download_url"]})
                            break
                ids = ids[len(results):]
                i += len(results)
            else:
                print(f"\nRequest fail: {response.text}")
                exit(1)

        print('Getting download urls... ', f"{i}/{targetAmount}")

        return mods

    def _download(self, mod: dict) -> None:
        """Downloads a mod"""
        url = f"https://mods.factorio.com{mod["download_url"]}"
        modName = mod["file_name"]
        if not os.path.exists("mods"):
            os.mkdir("mods")

        if not os.path.exists(f"mods/{modName}"):
            with requests.get(url, {"username": self._data["username"], "token": self._data["token"]}, stream=True) as r:
                r.raise_for_status()
                size = int(r.headers["Content-Length"])
                chunk_size = 8192
                with open(f"mods/{modName}", "wb") as f:
                    with Progress(*self._progressBarColumns) as progress:
                        task = progress.add_task(modName, total=size)
                        for chunck in r.iter_content(chunk_size=chunk_size):
                            if chunck:
                                f.write(chunck)
                                progress.update(task, advance=chunk_size)
                        progress.update(task, completed=size)


if __name__ == "__main__":
    dl = Downloader("fmods.txt", 1.1)
    dl.execute()

