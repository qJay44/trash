from os import scandir
from random import choice, randint
from config import *
import json
import requests


def chooseSound():
    response = requests.get("https://kingsc.net/ChatSounds.txt")
    if response.status_code != 200:
        print("Bad response")

    lines = [line.split('\t')[1].split(' ')[0] for line in response.text.splitlines()[3:]]

    return choice(lines)


def chooseHat():
    hats = ['afro', 'angel2', 'angelhead', 'anticross', 'arrow autism', 'aviators', 'azusa_big', 'baron_bunny_new', \
            'beerhat beret', 'booptail', 'camohat', 'cathead', 'cattail chef', 'clocknecklace', 'clown_wig', \
            'collar_pink', 'cophat cowboy', 'cross', 'crown', 'deal_with_it', 'devil2 devilhead', 'deviltail', \
            'devilwing', 'elf', 'fag fox_hat', 'fox_hat _b', 'gasmask_wh', 'goldhead', 'headcrab headphones', \
            'hood', 'inosuke', 'jamacahat2', 'jotaro_hat kermit_cap', 'kfcbucket', 'magic', 'mask', 'mic_chan padoru', \
            'pandahead' , 'paperbag', 'pighead', 'pigtail pirate2', 'pyramidhead_new', 'randoseru', 'randoseru_padoru', \
            'randoseru_s ricefarmer', 'santahat', 'santahat2', 'shades', 'stahlhelm sumb raro2', 'tank', 'tophat', 'tutu', \
            'tweedle ushanka', 'ushanka_2', 'viking', 'wehrmacht', 'wehrmacht2 wing_freedom ']

    return choice(hats)

modelDirs = [*scandir(MODELS_PATH1), *scandir(MODELS_PATH2)]
model = choice(modelDirs).name
name = chooseSound()
hat = chooseHat()

# Write vc voice and pitch to twlz config
with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
    vcDirs = [*scandir(VC_PATH)]
    vcVoice = choice(vcDirs).name[:-7]
    vcPitch = randint(60, 150)
    f.write(f".vc voice {vcVoice}\n.vc pitch {vcPitch}\n.skin -2\n.hat {hat}\n.trail random")

# Write model command to my.cfg
with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
    f.write(f"model {model}\nname {name}")

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
    f"hat {hat}\n"
)

