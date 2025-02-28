import requests
import pickle
from os.path import exists
from os import scandir

SV_PATH = r'C:/Program Files (x86)/Steam/steamapps/common/Sven Co-op/'

MODELS_PATH1    = rf'{SV_PATH}/svencoop_addon/models/player'
MODELS_PATH2    = rf'{SV_PATH}/svencoop_downloads/models/player'
MY_CFG_PATH     = rf'{SV_PATH}/svencoop/my.cfg'
KING_CFG_PATH   = rf'{SV_PATH}/svencoop/king.cfg'
VC_PATH         = rf'{SV_PATH}/svencoop_downloads/sound/vc/pack'

MODELS = [*scandir(MODELS_PATH1), *scandir(MODELS_PATH2)]

HATS = ['afro', 'angel2', 'angelhead', 'anticross', 'arrow autism', 'aviators', 'azusa_big', 'baron_bunny_new',
        'beerhat beret', 'booptail', 'camohat', 'cathead', 'cattail chef', 'clocknecklace', 'clown_wig',
        'collar_pink', 'cophat cowboy', 'cross', 'crown', 'deal_with_it', 'devil2 devilhead', 'deviltail',
        'devilwing', 'elf', 'fag fox_hat', 'fox_hat _b', 'gasmask_wh', 'goldhead', 'headcrab headphones',
        'hood', 'inosuke', 'jamacahat2', 'jotaro_hat kermit_cap', 'kfcbucket', 'magic', 'mask', 'mic_chan padoru',
        'pandahead' , 'paperbag', 'pighead', 'pigtail pirate2', 'pyramidhead_new', 'randoseru', 'randoseru_padoru',
        'randoseru_s ricefarmer', 'santahat', 'santahat2', 'shades', 'stahlhelm sumb raro2', 'tank', 'tophat', 'tutu',
        'tweedle ushanka', 'ushanka_2', 'viking', 'wehrmacht', 'wehrmacht2 wing_freedom ']

TRAIL_SPRITES = ['arrows', 'fatline', 'interlace', 'lightning', 'point', 'smokey', 'squarewave', 'svenlogo', 'thinline', 'voice']
TRAIL_PALETTES = [ 'anime', 'beach', 'cyberpunk', 'forest', 'goldfish', 'interceptor', 'intersex', 'lgbt', 'light', 'random',
                  'metro', 'moss', 'neonpunk', 'pansexual', 'pastel', 'seaweed', 'sugar', 'trap', 'wheel', 'white', 'winter']


def getChatSounds():
    response = requests.get(r'https://kingsc.net/ChatSounds.txt')
    if response.status_code != 200:
        print('Bad response')
    else:
        lines = [line.split('\t')[1].split(' ')[0] for line in response.text.splitlines()[3:]]
        with open('cs.pkl', 'wb') as f:
            pickle.dump(lines, f)


# [yellowygreen | yelloworange | yellowishorange | ...] -> [yellowygreen, yelloworange, yellowishorange, ...]
def convert(filename):
    with open(f'{filename}.txt', 'r') as fr:
        with open(f'{filename}.pkl', 'wb') as fw:
            pickle.dump(fr.read().replace('\n', '| ').split(' | '), fw)


if not exists('cs.pkl'):
    getChatSounds()

if not exists('colornames.pkl'):
    # The list itself should in the corresponding .txt file
    if not exists('colornames.txt'):
        print('missing colornames.txt')
        exit(1)
    convert('colornames')

# Large lists are stored in pickle files
CHAT_SOUNDS = (lambda: (f:=open('cs.pkl', 'rb'), pickle.load(f), f.close())[1])()
TRAIL_COLORNAMES = (lambda: (f:=open('colornames.pkl', 'rb'), pickle.load(f), f.close())[1])()

