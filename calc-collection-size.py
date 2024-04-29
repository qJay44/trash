from requests import post
from sys import argv
from math import floor


def main():
    collection = getCollectionDetails(argv[1])
    items = getPublishedFileDetails(collection)
    showTotalSize(items)


def getCollectionDetails(id):
    url = 'https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/'
    body = {'collectioncount': 1, 'publishedfileids[0]': id}

    return dict(post(url, body).json())['response']['collectiondetails'][0]['children']


def getPublishedFileDetails(collection):
    url = 'https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/'
    body = {'itemcount': len(collection)}
    for i, item in enumerate(collection):
        body[f'publishedfileids[{i}]'] = item['publishedfileid']

    return dict(post(url, body).json())['response']['publishedfiledetails']


def showTotalSize(items):
    total = 0.
    for item in items:
        if item['result'] == 1:
            total += float(item['file_size'])

    gb = total / 1e9
    mb = gb * 1000
    kb = mb * 1000
    totalBytes = kb * 1000

    msg = 'Total size: {:.2f} {}'

    if   floor(gb) > 1: print(msg.format(gb, 'GB'))
    elif floor(mb) > 1: print(msg.format(mb, 'MB'))
    elif floor(kb) > 1: print(msg.format(kb, 'KB'))
    else: print(msg.format(totalBytes, 'Bytes'))


main()

