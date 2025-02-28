from os import scandir
from random import choice, randint
from config import *
import json

tcolorname = choice(TRAIL_COLORNAMES)
tpalette = choice(TRAIL_PALETTES)
tsprite = choice(TRAIL_SPRITES)
model = choice(MODELS).name
name = choice(CHAT_SOUNDS)
hat = choice(HATS)

# Server config
with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
    vcDirs = [*scandir(VC_PATH)]
    vcVoice = choice(vcDirs).name[:-7]
    vcPitch = randint(60, 150)
    scfg = \
        f'say trail {tcolorname} {tsprite}\n' + \
        f'.vc voice {vcVoice}\n' + \
        f'.vc pitch {vcPitch}\n' + \
        f'.hat {hat}\n' + \
        f'.trail {tpalette}\n' + \
         '.skin -2'
    f.write(scfg)

# Client config
with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
    ccfg = f'model {model}\nname {name}'
    f.write(ccfg)

# Append used model to json
with open('used_models.json', 'r+') as f:
    data = json.load(f)

    if model not in data['models']:
        data['models'].append(model)

    f.seek(0)
    json.dump(data, f, indent=4)

print(f'{scfg}\n\n{ccfg}')

