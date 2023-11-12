import os
import subprocess
import vpk
import pathlib

VANILA_SOUNDS_FOLDER = 'C:\\Users\\gerku\\Documents\\non-project-trash\\vpk-nmrih\original\\firearms'
VANILA_DECREASED_SOUNDS_FOLDER = 'C:\\Users\\gerku\\Documents\\non-project-trash\\vpk-nmrih\original\\firearms-decreased'
ADDON_SOUNDS_FOLDER = 'C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\224260'
ADDON_DECREASED_SOUNDS_FOLDER = 'vpk-nmrih\\root'
DECREASE_FACTOR = 0.5


def deacreaseOriginalSounds():
    dirsPath = [os.path.join(VANILA_SOUNDS_FOLDER, name) for name in os.listdir(VANILA_SOUNDS_FOLDER)]
    os.makedirs(VANILA_DECREASED_SOUNDS_FOLDER, exist_ok=True)

    for folderPath in dirsPath:
        for file in os.listdir(folderPath):
            if 'fire' in file and not 'dryfire' in file:
                folder = folderPath.split(VANILA_SOUNDS_FOLDER)[1]
                os.makedirs(f'{VANILA_DECREASED_SOUNDS_FOLDER}\{folder}', exist_ok=True)
                subprocess.call(
                    [
                        'ffmpeg', '-hide_banner', '-y',
                        '-i', f'{folderPath}\{file}',
                        '-filter:a', f'volume={DECREASE_FACTOR}',
                        f'{VANILA_DECREASED_SOUNDS_FOLDER}{folder}\{file}'
                    ]
                )


def deacreaseAddonSounds():
    dirsPath = [os.path.join(ADDON_SOUNDS_FOLDER, name) for name in os.listdir(ADDON_SOUNDS_FOLDER)]

    for folderPath in dirsPath:
        for file in os.listdir(folderPath):
            if file[-3:] == 'vpk':
                pak = vpk.open(f'{folderPath}\{file}')
                pak.read_index()

                # Every existing file and folder in vpk file
                for k in pak.tree.keys():
                    if 'sound/weapons/firearms' in k:
                        path = pathlib.Path(k)
                        if 'fire' in str(path.stem) and not 'dryfire' in str(path.stem):
                            os.makedirs(f'{ADDON_DECREASED_SOUNDS_FOLDER}\{path.parent}', exist_ok=True)
                            tempFile = f'{ADDON_DECREASED_SOUNDS_FOLDER}\{path.parent}\{path.stem}_temp{path.suffix}'
                            pak.get_file(k).save(tempFile)
                            subprocess.call(
                                [
                                    'ffmpeg', '-hide_banner', '-y',
                                    '-i',
                                    tempFile,
                                    '-filter:a', f'volume={DECREASE_FACTOR}',
                                    tempFile.replace('_temp', '')
                                ]
                            )
                            os.remove(tempFile)

    newpak = vpk.new('.\\' + ADDON_DECREASED_SOUNDS_FOLDER)
    newpak.save('./vpk-nmrih/firearms-decreased-volume-sounds.vpk')


deacreaseOriginalSounds()
deacreaseAddonSounds()

