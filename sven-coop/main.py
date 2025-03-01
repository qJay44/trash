from random import choice, randint
from config import TRAIL_COLORNAMES, TRAIL_PALETTES, TRAIL_SPRITES, VC_NAMES, MODELS, CHAT_SOUNDS, HATS, KING_CFG_PATH, MY_CFG_PATH
import json

tcolorname = choice(TRAIL_COLORNAMES)
tpalette = choice(TRAIL_PALETTES)
tsprite = choice(TRAIL_SPRITES)
voice = choice(VC_NAMES).name[:-7]
model = choice(MODELS).name
name = choice(CHAT_SOUNDS)
hat = choice(HATS)
pitch = randint(60, 150)

# Server config
with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
    scfg = \
        f'say trail {tcolorname} {tsprite}\n' + \
        f'.flashlight {tcolorname}\n' + \
        f'.vc voice {voice}\n' + \
        f'.vc pitch {pitch}\n' + \
        f'.trail {tpalette}\n' + \
        f'.hat {hat}\n' + \
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

