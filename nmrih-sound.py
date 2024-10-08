# NOTE:
# - Vanila folder extracted manually (only folders should be in "firearms" folder)
# - Update the load order in NMRIH (Should last)

import os
import subprocess
import vpk
import pathlib
from sys import argv
from shutil import copy

VANILA_SOUNDS_FOLDER = 'vpk-nmrih\\original'
ADDON_SOUNDS_FOLDER = 'C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\224260'
NEW_SOUNDS_ROOT = 'vpk-nmrih\\root'
CUSTOM_VALUES = {
    'sks_fire_01.wav': 0.05,
    'glock_fire_01.wav': 0.1
}


def main():
    volumeValue = 0.5
    if (len(argv) == 2):
        try:
            volumeValue = max(min(float(argv[1]), 1.0), 0.0)
        except ValueError:
            print(f'Invalid given value ({argv[1]})')

    print(f'Volume value: {volumeValue}')

    handleVanillaSounds(volumeValue)
    handleAddonSounds(volumeValue)

    # Create and copy new vpk to the addons foler
    newPakName = 'firearms-decreased-volume-sounds.vpk'
    newPak = vpk.new(NEW_SOUNDS_ROOT)
    newPak.save('vpk-nmrih\\' + newPakName)
    copy(f'vpk-nmrih/{newPakName}', f'C:\\Program Files (x86)\\Steam\\steamapps\\common\\nmrih\\nmrih\\custom/{newPakName}')


def handleVanillaSounds(volumeValue):
    firearmsDir = VANILA_SOUNDS_FOLDER + '\\weapons\\firearms'
    dirsPath = [os.path.join(firearmsDir, name) for name in os.listdir(firearmsDir)]

    i = 1
    for folderPath in dirsPath:
        for file in os.listdir(folderPath):
            if 'fire' in file and not 'dryfire' in file:
                newFilePath = f'{NEW_SOUNDS_ROOT}\\sound\\weapons\\firearms/{folderPath.split(firearmsDir)[1]}'
                os.makedirs(newFilePath, exist_ok=True)
                subprocess.call(
                    [
                        'ffmpeg', '-hide_banner', '-y', '-loglevel', 'error',
                        '-i', f'{folderPath}/{file}',
                        '-filter:a', f'volume={CUSTOM_VALUES[file] if file in CUSTOM_VALUES.keys() else volumeValue}',
                        f'{newFilePath}/{file}'
                    ]
                )
                print('Vanila soudns handled: ', i, sep='', end='\r', flush=True)
                i += 1

    headpopDir = VANILA_SOUNDS_FOLDER + '\\physics\\flesh'

    for file in os.listdir(headpopDir):
        newFilePath = f'{NEW_SOUNDS_ROOT}\\sound\\physics\\flesh/{file}'
        subprocess.call(
            [
                'ffmpeg', '-hide_banner', '-y', '-loglevel', 'error',
                '-i', f'{headpopDir}/{file}',
                '-filter:a', f'volume={volumeValue}',
                newFilePath
            ]
        )
        print('Vanila soudns handled: ', i, sep='', end='\r', flush=True)
        i += 1

    print()


def handleAddonSounds(volumeValue):
    dirsPath = [os.path.join(ADDON_SOUNDS_FOLDER, name) for name in os.listdir(ADDON_SOUNDS_FOLDER)]

    i = 1
    for folderPath in dirsPath:
        for file in os.listdir(folderPath):
            # Make sure to operate on a vpk file, not its cache
            if file[-3:] == 'vpk':
                pak = vpk.open(f'{folderPath}/{file}')
                pak.read_index() # Init the tree

                # For every existing file and folder in a vpk file
                for pakFile in pak.tree.keys():
                    if 'sound/weapons/firearms' in pakFile:
                        path = pathlib.Path(pakFile)
                        if 'fire' in str(path.stem) and not 'dryfire' in str(path.stem):
                            os.makedirs(f'{NEW_SOUNDS_ROOT}/{path.parent}', exist_ok=True)
                            tempFile = f'{NEW_SOUNDS_ROOT}/{path.parent}/{path.stem}_temp{path.suffix}'
                            pak.get_file(pakFile).save(tempFile)
                            subprocess.call(
                                [
                                    'ffmpeg', '-hide_banner', '-y', '-loglevel', 'error',
                                    '-i', tempFile,
                                    '-filter:a', f'volume={volumeValue}',
                                    tempFile.replace('_temp', '')
                                ]
                            )
                            os.remove(tempFile)
                            print('Addon soudns handled: ', i, sep='', end='\r', flush=True)
                            i += 1
    print()


main()

