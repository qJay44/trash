from random import choice, randint
from config import COLORNAMES, TRAIL_PALETTES, TRAIL_SPRITES, VC_NAMES, HATS, KING_CFG_PATH, MY_CFG_PATH
import history


def create() -> tuple[str, str]:
    def roll(winVal, loseVal='', winTres=10): return winVal if randint(1, 100) < winTres else loseVal

    # Server config
    scfg = \
        'exec clear.cfg\n' + \
        roll(f'say trail {choice(COLORNAMES)} {choice(TRAIL_SPRITES)}\n') + \
        roll(f'.trail {choice(TRAIL_PALETTES)}\n') + \
        f'.vc voice {roll(choice(VC_NAMES).name[:-7], 'scientist')}\n' + \
        f'.vc pitch {roll(randint(40, 200), 100)}\n' + \
        f'.hat {roll(choice(HATS), 'off', 25)}\n'  + \
        f'.skin {roll(-2, 0)}\n' + \
        f'.color {roll(choice(['r', 'g', 'b', 'y']), 'off')}'

    # Client config
    ccfg = \
        f'model {history.choose('models')}\n' + \
        f'name {history.choose('names')}\n' + \
        f'topcolor {randint(0, 255)}\n' + \
        f'bottomcolor {randint(0, 255)}'

    return (scfg, ccfg)


def apply(scfg: str, ccfg: str) -> None:
    with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
        f.write(scfg)

    with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
        f.write(ccfg)

    history.write(scfg, ccfg)


if __name__ == '__main__':
    scfg, ccfg = create()
    apply(scfg, ccfg)

    print(f'{scfg}\n\n{ccfg}')
    print(f'models left: {history.length['models']}')
    print(f'names left: {history.length['names']}')

