from os import scandir
from random import choice, randint
from config import SC_PATH
from create import create
import json


class Dop:
    # Load all dops
    def __init__(self) -> None:
        DOPS_PATH = rf'{SC_PATH}/svencoop/dop'
        self.real: list[str] = []
        self.created: list[dict[str, str]] = []

        for file in [*scandir(DOPS_PATH)]:
            with open(f'{DOPS_PATH}/{file.name}', 'r', encoding='utf-8') as f:
                self.real.append(f.read())

        with open('history.json', 'r', encoding='utf-8') as f:
            cfgFmt = 'exec clear.cfg\n%s\n%s'
            self.created = [cfgFmt % (cfgData['scfg'], cfgData['ccfg']) for cfgData in json.load(f)['cfgs']]

    # Returns concatenated string with both client cfg and server cfg
    # (Should look like one from the "dop" folder)
    def choose(self) -> str:
        percent = randint(1, 100)

        if percent >= 10:
            return choice(self.real)
        if percent >= 2:
            return choice(self.created)
        else:
            return 'exec clear.cfg\n{}\n{}'.format(*create())

    @staticmethod
    def apply(cfg) -> None:
        with open(rf'{SC_PATH}/svencoop/dop.cfg', 'w', encoding='utf-8') as f:
            f.write(cfg)


if __name__ == '__main__':
    print(Dop().choose())

