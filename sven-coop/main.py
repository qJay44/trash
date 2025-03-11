from random import choice, randint
from config import TRAIL_COLORNAMES, TRAIL_PALETTES, TRAIL_SPRITES, VC_NAMES, MODELS, NICKNAMES, HATS, KING_CFG_PATH, MY_CFG_PATH
import json

tcolorname = choice(TRAIL_COLORNAMES)
tpalette = choice(TRAIL_PALETTES)
tsprite = choice(TRAIL_SPRITES)
voice = choice(VC_NAMES).name[:-7]
model = choice(MODELS).name
name = choice(NICKNAMES)
hat = choice(HATS)
pitch = randint(60, 150)

# Server config
with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
    def roll(win, lose=''): return win if randint(0, 100) < 10 else lose

    scfg = \
        roll(f'say trail {tcolorname} {tsprite}\n') + \
        roll(f'.trail {tpalette}\n') + \
        f'.vc voice {roll(voice, 'scientist')}\n' + \
        f'.vc pitch {roll(pitch, 100)}\n' + \
        f'.hat {roll(hat, 'off')}\n'  + \
        f'.skin {roll(-2, 0)}\n' + \
        '.color off\n' + \
        '.e off'
    f.write(scfg)

# Client config
with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
    ccfg = f'model {model}\nname {name}'
    f.write(ccfg)

# Append used model to json
with open('history.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
    data['cfgs'].append({'scfg': scfg, 'ccfg': ccfg})
    f.seek(0)
    json.dump(data, f, indent=4)

print(f'{scfg}\n\n{ccfg}')

