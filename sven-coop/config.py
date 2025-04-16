import requests
import pickle
import re
from random import randint
from os.path import exists
from os import scandir

SC_PATH = r'C:/Program Files (x86)/Steam/steamapps/common/Sven Co-op/'

MODELS_PATH1  = rf'{SC_PATH}/svencoop_addon/models/player'
MODELS_PATH2  = rf'{SC_PATH}/svencoop_downloads/models/player'
MY_CFG_PATH   = rf'{SC_PATH}/svencoop/my.cfg'
KING_CFG_PATH = rf'{SC_PATH}/svencoop/king.cfg'
VC_PATH       = rf'{SC_PATH}/svencoop_downloads/sound/vc/pack'

MODELS = [*scandir(MODELS_PATH1), *scandir(MODELS_PATH2)]
VC_NAMES = [*scandir(VC_PATH)]

HATS = ['afro', 'angel2', 'angelhead', 'anticross', 'arrow', 'autism', 'aviators', 'azusa_big', 'baron_bunny_new', 'beerhat', 'beret', 'booptail', 'bunnymask', 'camohat', 'cathead',
        'cattail', 'chef', 'clocknecklace', 'clown_wig', 'collar_pink', 'cophat', 'cowboy', 'cross', 'crown', 'deal_with_it', 'devil2', 'devilhead', 'deviltail', 'devilwing', 'elf',
        'fag', 'fox_hat', 'fox_hat_b', 'gasmask_wh', 'goldhead', 'headcrab', 'headphones', 'hood', 'inosuke', 'jamacahat2', 'jotaro_hat', 'kermit_cap', 'kfcbucket', 'magic', 'mask',
        'mic_chan', 'padoru', 'pandahead', 'paperbag', 'pighead', 'pigtail', 'pirate2', 'pyramidhead_new', 'randoseru', 'randoseru_padoru', 'randoseru_s', 'ricefarmer', 'santahat',
        'santahat2', 'shades', 'stahlhelm', 'sumbraro2', 'tank', 'tophat', 'tutu', 'tweedle', 'ushanka', 'ushanka_2', 'viking', 'wehrmacht', 'wehrmacht2', 'wing_freedom']

PETS = ['aliengrunt', 'archer', 'babyheadcrab', 'bigmomma', 'bullsquid', 'chatarou', 'chumtoad', 'cockroach', 'controller', 'dog', 'floater', 'gargantua',
        'gura', 'headcrab', 'hk416', 'houndeye', 'karen', 'loader', 'miketama', 'pizzashopowner', 'rat', 'skeleton', 'stukabat', 'touhou_chen', 'xenbat']

TRAIL_SPRITES = ['arrows', 'fatline', 'interlace', 'lightning', 'point', 'smokey', 'squarewave', 'svenlogo', 'thinline', 'voice']

TRAIL_PALETTES = ['anime', 'beach', 'cyberpunk', 'forest', 'goldfish', 'interceptor', 'intersex', 'lgbt', 'light', 'random',
                  'metro', 'moss', 'neonpunk', 'pansexual', 'pastel', 'seaweed', 'sugar', 'trap', 'wheel', 'white', 'winter']


def downloadCS():
    response = requests.get(r'https://www.kingsc.net/ChatSounds.txt')
    if response.status_code != 200:
        print('Bad response')
        exit(1)
    else:
        lines = re.findall(r'(?:^\d+\s)([^ ]+)', response.text, re.MULTILINE)
        with open('cs.pkl', 'wb') as f:
            pickle.dump(lines, f)


# [yellowygreen | yelloworange | yellowishorange | ...] -> [yellowygreen, yelloworange, yellowishorange, ...]
def convert(filename):
    with open(f'{filename}.txt', 'r') as fr:
        with open(f'{filename}.pkl', 'wb') as fw:
            names = re.findall(r'\w+', fr.read(), re.MULTILINE)
            pickle.dump(names, fw)


if not exists('cs.pkl'):
    downloadCS()

if not exists('colornames.pkl'):
    # The list itself should in the corresponding .txt file
    if not exists('colornames.txt'):
        print('missing colornames.txt')
        exit(1)
    convert('colornames')

# Large lists are stored in pickle files
NICKNAMES = (lambda: (f:=open('cs.pkl' if randint(0, 100) < 5 else 'hypixel-players.pkl', 'rb'), pickle.load(f), f.close())[1])()
COLORNAMES = (lambda: (f:=open('colornames.pkl', 'rb'), pickle.load(f), f.close())[1])()
