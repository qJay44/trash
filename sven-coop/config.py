import requests
import pickle
import re
from os.path import exists
from os import scandir

SC_PATH = r'C:/Program Files (x86)/Steam/steamapps/common/Sven Co-op/'

MODELS_PATH1  = rf'{SC_PATH}/svencoop_addon/models/player'
MODELS_PATH2  = rf'{SC_PATH}/svencoop_downloads/models/player'
MY_CFG_PATH   = rf'{SC_PATH}/svencoop/my.cfg'
KING_CFG_PATH = rf'{SC_PATH}/svencoop/king.cfg'
VC_PATH       = rf'{SC_PATH}/svencoop_downloads/sound/vc/pack'

HATS = [
    'afro', 'angel2', 'angelhead', 'anticross', 'arrow', 'autism', 'aviators', 'azusa_big', 'baron_bunny_new',
    'beerhat', 'beret', 'booptail', 'bunnymask', 'camohat', 'cathead', 'cattail', 'chef', 'clocknecklace',
    'clown_wig', 'collar_pink', 'cophat', 'cowboy', 'cross', 'crown', 'deal_with_it', 'devil2', 'devilhead',
    'deviltail', 'devilwing', 'elf', 'fag', 'fox_hat', 'fox_hat_b', 'gasmask_wh', 'goldhead', 'headcrab',
    'headphones', 'hood', 'inosuke', 'jamacahat2', 'jotaro_hat', 'kermit_cap', 'kfcbucket', 'magic', 'mask',
    'mic_chan', 'padoru', 'pandahead', 'paperbag', 'pighead', 'pigtail', 'pirate2', 'pyramidhead_new', 'randoseru',
    'randoseru_padoru', 'randoseru_s', 'ricefarmer', 'santahat', 'santahat2', 'shades', 'stahlhelm', 'sumbraro2',
    'tank', 'tophat', 'tutu', 'tweedle', 'ushanka', 'ushanka_2', 'viking', 'wehrmacht', 'wehrmacht2', 'wing_freedom'
]

PETS = [
    'aliengrunt', 'archer', 'babyheadcrab', 'bigmomma', 'bullsquid', 'chatarou', 'chumtoad', 'cockroach',
    'controller', 'dog', 'floater', 'gargantua', 'gura', 'headcrab', 'hk416', 'houndeye', 'karen',
    'loader', 'miketama', 'pizzashopowner', 'rat', 'skeleton', 'stukabat', 'touhou_chen', 'xenbat'
]

VC_VOICES = [
    'scientist', 'hl_usadapekora', 'necoarc', 'hl_inugamikorone', 'gachi', 'nagatoro', 'hl_hoshoumarine',
    'cracklife', 'hl_uruharushia', 'uboa', 'portalturret', 'terrydavis', 'usec', 'soldier', 'ark_lappland',
    'l4d_bill', 'pl_maeve', 'fathergrigori', 'monster_school', 'mute', 'kujoukaren', 'chadwarden', 'lamardavis',
    'infantry', 'postaldude', 'jcdenton', 'turklayf', 'l4d_louis', 'bandit', 'shocktrooper', 'al_nagato',
    'counterstrikebot', 'humangrunt', 'l4d_zoey', 'robotgrunt', 'tourettesguy', 'deadpool', 'bodyguard',
    'hev_suit', 'gabrielangelos', 'pd2_dallas', 'bear', 'dio_sc', 'dio_pb', 'carljohnson', 'arnold_schwarzenegger',
    'barney', 'ba_koyuki', 'pd2_jacket', 'mason_maa', 'otis', 'duke3d', 'salem', 'kingpinfargus', 'sgthartmann',
    'ba_saki', 'al_ayanami', 'hl2femalecitizen', 'ba_hoshino', 'ba_momoi', 'glados', 'kf_ostrich', 'agathaknight',
    'baldisbasics', 'drcoomer', 'ba_mutsuki', 'gg_hk416', 'counterstrike', 'ba_ako', 'wesker', 'kf_malevoiceone',
    'ba_yuzu', 'gman', 'bigboss', 'csgoseparatist', 'ark_texas', 'dukenukem', 'ba_rio', 'ssh', 'vox', 'brocksamson',
    'tf2medic', 'tf2spy', 'ellisl4d', 'benrey', 'serioussam', 'cavejohnson', 'beck', 'pl_raevemaeve', 'ba_hina',
    'quiet', 'ba_midori', 'pd2_jimmy', 'jamiemod', 'ba_aru', 'phoenix', 'rochellel4d', 'ba_nonomi', 'ba_moe',
    'drbreen', 'ba_shiroko', 'ba_kayoko', 'tf2demoman', 'tf2merasmus', 'ba_miyako', 'ba_miyu', 'ba_arona',
    'ba_chinatsu', 'ba_haruka', 'tf2soldier', 'ba_arisu', 'tf2scout', 'ba_serika', 'ba_iori', 'ba_ayane'
]

TRAIL_SPRITES = ['arrows', 'fatline', 'interlace', 'lightning', 'point', 'smokey', 'squarewave', 'svenlogo', 'thinline', 'voice']

TRAIL_PALETTES = ['anime', 'beach', 'cyberpunk', 'forest', 'goldfish', 'interceptor', 'intersex', 'lgbt', 'light', 'random',
                  'metro', 'moss', 'neonpunk', 'pansexual', 'pastel', 'seaweed', 'sugar', 'trap', 'wheel', 'white', 'winter']


def downloadCS():
    print("Donwloading ChatSounds")
    response = requests.get(r'https://www.kingsc.net/ChatSounds.txt')
    if response.status_code != 200:
        print('Bad response')
        exit(1)
    else:
        lines = re.findall(r'(?:^\d+\s)([^ ]+)', response.text, re.MULTILINE)
        with open('cs.pkl', 'wb') as f:
            pickle.dump(lines, f)

    print("Done")


# [yellowygreen | yelloworange | yellowishorange | ...] -> [yellowygreen, yelloworange, yellowishorange, ...]
def convert(filename):
    print(f"Converting [{filename}]")
    with open(f'{filename}.txt', 'r') as fr:
        with open(f'{filename}.pkl', 'wb') as fw:
            names = re.findall(r'\w+', fr.read(), re.MULTILINE)
            pickle.dump(names, fw)

    print("Done")

def getModels():
    return [*scandir(MODELS_PATH1), *scandir(MODELS_PATH2)]


if not exists('cs.pkl'):
    downloadCS()

if not exists('colornames.pkl'):
    # The list itself should be in the corresponding .txt file
    if not exists('colornames.txt'):
        print('missing colornames.txt')
        exit(1)
    convert('colornames')

COLORNAMES = (lambda: (f:=open('colornames.pkl', 'rb'), pickle.load(f), f.close())[1])()

if __name__ == '__main__':
    print("end")

