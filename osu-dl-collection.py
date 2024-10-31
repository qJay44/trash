import re
import requests
import os
from sys import argv
from rich.default_styles import DEFAULT_STYLES
from rich.style import Style

# The only way to change styles of some columns without modifying (within) the library
DEFAULT_STYLES["progress.download"] = Style(color="cyan3")
DEFAULT_STYLES["progress.data.speed"] = Style(color="pink3")

# This package uses "DEFAULT_STYLES" so have to import it after the changes
from rich.progress import BarColumn, DownloadColumn, Progress, TextColumn, TransferSpeedColumn # type: ignore # noqa: E402

dlProgress = 1
dlProgressTarget = 1
progressBarColumns= [
    TextColumn("[cyan][progress.description]{task.description}"),
    BarColumn(),
    DownloadColumn(),
    TransferSpeedColumn()
]


def main():
    global dlProgressTarget

    if (len(argv) != 3):
        print(f'Wrong arguments(ex.: {argv[0]} "client_id" "client_secret")')
        exit(1)

    client = {
        'id': argv[1],
        'secret': argv[2],
    }

    beatmaps = getBeatmaps(getToken(client))
    dlProgressTarget = len(beatmaps)

    for b in beatmaps:
        download(b)

    print(f'Done [{dlProgress}/{dlProgressTarget}]')


def getToken(client):
    url = 'https://osu.ppy.sh/oauth/token'
    data = f'client_id={client['id']}&client_secret={client['secret']}&grant_type=client_credentials&scope=public'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url=url, data=data, headers=headers)

    if response.status_code == 401:
        print('Error: Wrong credentials')
    elif response.status_code == 200:
        return response.json()['access_token']
    else:
        print('Error: Got unexpected response when getting token')
    exit(1)


def getBeatmaps(token):
    with open('collection.db', 'r') as f:
        checksums = re.findall(r'(?:[a-z]|\d){32}', f.read())

    beatmaps = []
    notFound = 0
    url = 'https://osu.ppy.sh/api/v2/beatmaps/lookup'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    for i, c in enumerate(checksums, start=1):
        print('Getting download urls... ', f"{i}/{len(checksums)}", sep='', end='\r', flush=True)
        response = requests.get(url=url, params={'checksum': c}, headers=headers)

        if response.status_code == 200:
            data = response.json()
            beatmaps.append({
                'id': data['beatmapset_id'],
                'artist': data['beatmapset']['artist'],
                'title': data['beatmapset']['title'],
            })
        else:
            notFound += 1

    print()
    print(f'Not found maps: {notFound}')

    return beatmaps


def download(beatmap):
    global dlProgress, dlProgressTarget

    if not os.path.exists('beatmaps'):
        os.mkdir('beatmaps')

    name = f'{beatmap['id']} {beatmap['artist']} - {beatmap['title']}.osz'

    # TODO: encoded names
    if not os.path.exists('beatmaps/' + name):
        with requests.get(f'https://catboy.best/d/{beatmap['id']}', stream=True) as r:
            r.raise_for_status()
            size = int(r.headers['Content-Length'])
            chunkSize = 8192
            with open('beatmaps/' + name, 'wb') as f:
                with Progress(*progressBarColumns) as progress:
                    task = progress.add_task(f'[{dlProgress}/{dlProgressTarget}] {name}', total=size)
                    for chunk in r.iter_content(chunk_size=chunkSize):
                        if chunk:
                            f.write(chunk)
                            progress.update(task, advance=chunkSize)
                    progress.update(task, completed=size)
    dlProgress += 1


main()

