from os import scandir
from random import choice, randint
from config import *
import json


def fromWords(f):
    words = f.read().split(" ")

    return choice(words)


def fromChars(f):
    text = f.read()
    chars = [choice(text) for _ in range(1, randint(1, 25))]

    return "".join(chars)


def fromSounds():
    # Folders will be also here but idc
    soundFiles = [
        *scandir(TWLZ_SOUND_PATH),
        *scandir(TWLZ_SOUND_PATH + "\plugins"),
        *scandir(TWLZ_SOUND_PATH + "\stolen")
    ]

    return choice(soundFiles).name[:-4]


modelDirs = [*scandir(MODELS_PATH1), *scandir(MODELS_PATH2)]
model = choice(modelDirs).name
name = fromSounds()

# with open('text.txt', 'r', encoding='utf-8') as f:
#     name = choice((fromWords, fromChars))(f)

# Write vc voice and pitch to twlz config
with open(TWLZ_CFG_PATH, 'w', encoding='utf-8') as f:
    vcDirs = [*scandir(VC_PATH)]
    vcVoice = choice(vcDirs).name[:-7]
    vcPitch = randint(60, 150)
    f.write(
        f".vc voice {vcVoice}\n.vc pitch {vcPitch}"
    )

# Write model command to my.cfg
with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
    f.write(
        f"model {model}\nname {name}"
    )

# Append used model to json
with open('used_models.json', 'r+') as f:
    data = json.load(f)

    if model not in data['models']:
        data['models'].append(model)

    f.seek(0)
    json.dump(data, f, indent=4)

print(
    f"model {model}\n"
    f"name {name}\n"
    f".vc voice {vcVoice}\n"
    f".vc pitch {vcPitch}\n"
)

