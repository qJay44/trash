import re
import requests
import os
import aiohttp
import asyncio
from validate_filename import validate
from sys import argv
from rich.default_styles import DEFAULT_STYLES
from rich.style import Style

# The only way to change styles of some columns without modifying (within) the library
DEFAULT_STYLES["progress.download"] = Style(color="cyan3")
DEFAULT_STYLES["progress.data.speed"] = Style(color="pink3")

# This package uses "DEFAULT_STYLES" so have to import it after the changes
from rich.progress import BarColumn, DownloadColumn, Progress, TextColumn, TransferSpeedColumn # type: ignore # noqa: E402

notFound = []
gatherProgress = 0
gatherProgressTarget = 0
dlProgress = 1
dlProgressTarget = 1
progressBarColumns= [
    TextColumn("[cyan][progress.description]{task.description}"),
    BarColumn(),
    DownloadColumn(),
    TransferSpeedColumn()
]


async def main():
    global dlProgressTarget

    if (len(argv) != 3):
        print(f'Wrong arguments(ex.: {argv[0]} "client_id" "client_secret")')
        exit(1)

    client = {
        'id': argv[1],
        'secret': argv[2],
    }

    async with aiohttp.ClientSession() as session:
        beatmaps = await getBeatmaps(session, getToken(client))

    dlProgressTarget = len(beatmaps)

    print('Downloading beatmaps...')
    for b in beatmaps:
        if b:
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


async def getBeatmap(session, **kwargs):
    global notFound, gatherProgress, gatherProgressTarget
    async with session.get(url=kwargs['url'], params=kwargs['params'], headers=kwargs['headers']) as response:
        if response.status == 200:
            data = await response.json()
            return {
                'id': data['beatmapset_id'],
                'artist': data['beatmapset']['artist'],
                'title': data['beatmapset']['title']
            }

        notFound.append(kwargs['params']['checksum'])

        gatherProgress += 1
        print('Getting beatmap urls... ', f"[{gatherProgress}/{gatherProgressTarget}]", sep='', end='\r', flush=True)

        return False


async def getBeatmaps(session, token):
    global notFound, gatherProgressTarget
    with open('collection.db', 'r') as f:
        checksums = re.findall(r'(?:[a-z]|\d){32}', f.read())

    url = 'https://osu.ppy.sh/api/v2/beatmaps/lookup'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    tasks = []
    for c in checksums:
        #response = requests.get(url=url, params={'checksum': c}, headers=headers)
        task = asyncio.create_task(getBeatmap(session, url=url, params={'checksum': c}, headers=headers))
        tasks.append(task)

    gatherProgressTarget = len(checksums)
    beatmaps = await asyncio.gather(*tasks)

    print('Getting beatmap urls... ', f"[{gatherProgress}/{gatherProgressTarget}]", sep='', end='\r', flush=True)
    print()
    print(f'Not found maps: {len(notFound)}')

    if notFound:
        with open('temp_osuNotFound.txt', 'w') as f:
            f.write('\n'.join(notFound))

    return beatmaps


def download(beatmap):
    global dlProgress, dlProgressTarget

    if not os.path.exists('beatmaps'):
        os.mkdir('beatmaps')

    filename = validate(f'{beatmap['id']} {beatmap['artist']} - {beatmap['title']}.osz')

    if not os.path.exists(f'{os.getenv('LOCALAPPDATA')}/osu!/Songs/{filename}') and not os.path.exists('beatmaps/' + filename):
        with requests.get(f'https://catboy.best/d/{beatmap['id']}', stream=True) as r:
            r.raise_for_status()
            size = int(r.headers['Content-Length'])
            chunkSize = 8192
            with open('beatmaps/' + filename, 'wb') as f:
                with Progress(*progressBarColumns) as progress:
                    task = progress.add_task(f'[{dlProgress}/{dlProgressTarget}] {filename}', total=size)
                    for chunk in r.iter_content(chunk_size=chunkSize):
                        if chunk:
                            f.write(chunk)
                            progress.update(task, advance=chunkSize)
                    progress.update(task, completed=size)
    dlProgress += 1


asyncio.run(main())

