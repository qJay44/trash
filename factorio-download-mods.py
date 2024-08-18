# https://wiki.factorio.com/Mod_portal_API

import json
import os
import requests
from bs4 import BeautifulSoup


class Downloader:
    def __init__(self, file: str, gameVersion: float) -> None:
        # Get player token and username
        with open(f"{os.getenv('APPDATA')}\\Factorio\\player-data.json", "r", encoding="utf-8") as f:
            playerDataJson = json.load(f)
            self._data = dict()
            self._data["username"] = playerDataJson["service-username"]
            self._data["token"] = playerDataJson["service-token"]
            self._data["version"] = gameVersion
            self._data["modsFile"] = file

    def execute(self) -> None:
        for mod in self._fetch(self._find()):
            self._download(mod)

    # Get mods ids from a first result on the search webpage
    def _find(self) -> list[str]:
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

    # Get mods info
    def _fetch(self, ids: list[str]) -> list[dict]:
        mods = []
        i = 0
        targetAmount = len(ids)

        # Using while loop since maximum mods retrieved per request is 25
        while len(ids) > 0:
            print('Getting donwload urls... ', f"{i}/{targetAmount}", sep='', end='\r', flush=True)
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

        print('Getting donwload urls... ', f"{i}/{targetAmount}")

        return mods

    def _download(self, mod: dict) -> None:
        url = f"https://mods.factorio.com{mod["download_url"]}"
        if not os.path.exists("mods"):
            os.mkdir("mods")

        # TODO: Add progress bar
        if not os.path.exists(f"mods/{mod["file_name"]}"):
            response = requests.get(url, {"username": self._data["username"], "token": self._data["token"]}, stream=True)
            with open(f"mods/{mod["file_name"]}", "wb") as f:
                f.write(response.content)


if __name__ == "__main__":
    dl = Downloader("fmods2.txt", 1.1)
    dl.execute()

