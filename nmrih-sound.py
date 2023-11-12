import os
import subprocess
import vpk
import pathlib

VANILA_SOUNDS_FOLDER = 'vpk-nmrih\\original\\firearms'
ADDON_SOUNDS_FOLDER = 'C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\224260'
NEW_SOUNDS_ROOT = 'vpk-nmrih\\root'
VOLUME_VALUE = 0.2


def deacreaseOriginalSounds():
    dirsPath = [os.path.join(VANILA_SOUNDS_FOLDER, name) for name in os.listdir(VANILA_SOUNDS_FOLDER)]

    for folderPath in dirsPath:
        for file in os.listdir(folderPath):
            if 'fire' in file and not 'dryfire' in file:
                newFilePath = f'{NEW_SOUNDS_ROOT}\\sound\\weapons\\firearms\{folderPath.split(VANILA_SOUNDS_FOLDER)[1]}'
                os.makedirs(newFilePath, exist_ok=True)
                subprocess.call(
                    [
                        'ffmpeg', '-hide_banner', '-y',
                        '-i', f'{folderPath}\{file}',
                        '-filter:a', f'volume={VOLUME_VALUE}',
                        f'{newFilePath}\{file}'
                    ]
                )


def deacreaseAddonSounds():
    dirsPath = [os.path.join(ADDON_SOUNDS_FOLDER, name) for name in os.listdir(ADDON_SOUNDS_FOLDER)]

    for folderPath in dirsPath:
        for file in os.listdir(folderPath):
            # Make sure to operate on a vpk file, not its cache
            if file[-3:] == 'vpk':
                pak = vpk.open(f'{folderPath}\{file}')
                pak.read_index() # Init the tree

                # For every existing file and folder in a vpk file
                for pakFile in pak.tree.keys():
                    if 'sound/weapons/firearms' in pakFile:
                        path = pathlib.Path(pakFile)
                        if 'fire' in str(path.stem) and not 'dryfire' in str(path.stem):
                            os.makedirs(f'{NEW_SOUNDS_ROOT}\{path.parent}', exist_ok=True)
                            tempFile = f'{NEW_SOUNDS_ROOT}\{path.parent}\{path.stem}_temp{path.suffix}'
                            pak.get_file(pakFile).save(tempFile)
                            subprocess.call(
                                [
                                    'ffmpeg', '-hide_banner', '-y',
                                    '-i', tempFile,
                                    '-filter:a', f'volume={VOLUME_VALUE}',
                                    tempFile.replace('_temp', '')
                                ]
                            )
                            os.remove(tempFile)

    newPak = vpk.new(NEW_SOUNDS_ROOT)
    newPak.save('vpk-nmrih/firearms-decreased-volume-sounds.vpk')


# deacreaseOriginalSounds()
deacreaseAddonSounds()

