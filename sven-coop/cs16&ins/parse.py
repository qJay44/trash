import re
import json

FILES16_ROOT = r'C:\Users\q44\Downloads\-SC-Counter-Strike-1.6-Weapons-Project-main\scripts\maps\cs16'
FILES_INS_ROOT = r'C:\Users\q44\Downloads\-SC-Insurgency-Weapons-Project-master\scripts\maps\ins2'

files16 = [
    r'rifl\weapon_sg552.as',
    r'shot\weapon_xm1014.as',
    r'lmg\weapon_csm249.as',
    r'misc\weapon_hegrenade.as',
    r'pist\weapon_usp.as',
    r'snip\weapon_sg550.as',
    r'rifl\weapon_famas.as',
    r'rifl\weapon_ak47.as',
    r'rifl\weapon_aug.as',
    r'pist\weapon_p228.as',
    r'rifl\weapon_galil.as',
    r'snip\weapon_g3sg1.as',
    r'snip\weapon_awp.as',
    r'rifl\weapon_m4a1.as',
    r'snip\weapon_scout.as',
    r'pist\weapon_csglock18.as',
    r'melee\weapon_csknife.as',
    r'pist\weapon_dualelites.as',
    r'misc\weapon_c4.as',
    r'smg\weapon_mp5navy.as',
    r'shot\weapon_m3.as',
    r'smg\weapon_p90.as',
    r'smg\weapon_mac10.as',
    r'pist\weapon_csdeagle.as',
    r'pist\weapon_fiveseven.as',
    r'smg\weapon_tmp.as',
    r'smg\weapon_ump45.as',
]

filesIns = [
    r'rifle\weapon_ins2svt40.as',
    r'srifl\weapon_ins2mosin.as',
    r'srifl\weapon_ins2m40a1.as',
    r'rifle\weapon_ins2kar98k.as',
    r'srifl\weapon_ins2m21.as',
    r'shotg\weapon_ins2saiga12.as',
    r'srifl\weapon_ins2g43.as',
    r'handg\weapon_ins2webley.as',
    r'smg\weapon_ins2ump45.as',
    r'srifl\weapon_ins2dragunov.as',
    r'rifle\weapon_ins2garand.as',
    r'shotg\weapon_ins2m590.as',
    r'rifle\weapon_ins2enfield.as',
    r'brifl\weapon_ins2scarh.as',
    r'smg\weapon_ins2ppsh41.as',
    r'arifl\weapon_ins2stg44.as',
    r'handg\weapon_ins2vp70.as',
    r'shotg\weapon_ins2m1014.as',
    r'smg\weapon_ins2mp7.as',
    r'arifl\weapon_ins2f2000.as',
    r'shotg\weapon_ins2ithaca.as',
    r'arifl\weapon_ins2m16a4.as',
    r'brifl\weapon_ins2m14ebr.as',
    r'arifl\weapon_ins2asval.as',
    r'brifl\weapon_ins2g3a3.as',
    r'brifl\weapon_ins2fnfal.as',
    r'brifl\weapon_ins2fg42.as',
    r'handg\weapon_ins2usp.as',
    r'arifl\weapon_ins2an94.as',
    r'handg\weapon_ins2c96.as',
    r'handg\weapon_ins2python.as',
    r'handg\weapon_ins2beretta.as',
    r'shotg\weapon_ins2coach.as',
    r'handg\weapon_ins2makarov.as',
    r'smg\weapon_ins2greasegun.as',
    r'smg\weapon_ins2mp5sd.as',
    r'smg\weapon_ins2m1928.as',
    r'smg\weapon_ins2l2a3.as',
    r'smg\weapon_ins2mp40.as',
    r'smg\weapon_ins2mp5k.as',
    r'handg\weapon_ins2m29.as',
    r'arifl\weapon_ins2akm.as',
    r'arifl\weapon_ins2groza.as',
    r'arifl\weapon_ins2ak74.as',
    r'arifl\weapon_ins2galil.as',
    r'arifl\weapon_ins2ak12.as',
    r'arifl\weapon_ins2m16a1.as',
    r'smg\weapon_ins2mp18.as',
    r'explo\weapon_ins2m79.as',
    r'explo\weapon_ins2law.as',
    r'arifl\weapon_ins2l85a2.as',
    r'explo\weapon_ins2mk2.as',
    r'explo\weapon_ins2pzschreck.as',
    r'explo\weapon_ins2pzfaust.as',
    r'handg\weapon_ins2deagle.as',
    r'explo\weapon_ins2at4.as',
    r'explo\weapon_ins2rpg7.as',
    r'handg\weapon_ins2glock17.as',
    r'handg\weapon_ins2m1911.as',
    r'explo\weapon_ins2stick.as',
    r'explo\weapon_ins2rgo.as',
    r'melee\weapon_ins2kabar.as',
    r'explo\weapon_ins2m2.as',
    r'melee\weapon_ins2knuckles.as',
    r'melee\weapon_ins2kukri.as',
    r'carbn\weapon_ins2aks74u.as',
    r'carbn\weapon_ins2g36c.as',
    r'carbn\weapon_ins2c96carb.as',
    r'carbn\weapon_ins2m4a1.as',
    r'lmg\weapon_ins2rpk.as',
    r'carbn\weapon_ins2m1a1para.as',
    r'carbn\weapon_ins2mk18.as',
    r'lmg\weapon_ins2lewis.as',
    r'lmg\weapon_ins2m60.as',
    r'lmg\weapon_ins2pkm.as',
    r'carbn\weapon_ins2sks.as',
    r'lmg\weapon_ins2m249.as',
    r'lmg\weapon_ins2mg34.as',
    r'lmg\weapon_ins2mg42.as',
]

insCost = {
    r'svt40': (290, 30),
    r'mosin': (320, 15),
    r'm40a1': (305, 10),
    r'kar98k': (240, 10, 30),
    r'm21': (350, 20),
    r'saiga12': (1001, 80), # (725, 80)
    r'g43': (340, 20),
    r'webley': (160, 10),
    r'ump45': (165, 20),
    r'dragunov': (360, 30),
    r'garand': (255, 15),
    r'm590': (285, 50),
    r'enfield': (270, 20),
    r'scarh': (350, 20),
    r'ppsh41': (235, 50),
    r'stg44': (290, 30),
    r'vp70': (170, 20),
    r'm1014': (330, 45),
    r'mp7': (315, 45),
    r'f2000': (265, 30),
    r'ithaca': (275, 40),
    r'm16a4': (325, 30, 30),
    r'm14ebr': (345, 20),
    r'asval': (230, 20),
    r'g3a3': (335, 20),
    r'fnfal': (330, 20),
    r'fg42': (360, 35),
    r'usp': (145, 10),
    r'an94': (300, 30),
    r'c96': (175, 15),
    r'python': (180, 15),
    r'beretta': (130, 15),
    r'coach': (295, 20),
    r'makarov': (100, 5),
    r'greasegun': (170, 25),
    r'mp5sd': (190, 20),
    r'm1928': (255, 50),
    r'l2a3': (195, 30),
    r'mp40': (185, 25),
    r'mp5k': (175, 20),
    r'm29': (190, 20),
    r'akm': (350, 30, 30),
    r'groza': (320, 20, 30),
    r'ak74': (285, 30),
    r'galil': (260, 35),
    r'ak12': (275, 30),
    r'm16a1': (310, 20, 30),
    r'mp18': (180, 15),
    r'm79': (450, 30, 30),
    r'law': (425),
    r'l85a2': (335, 30, 30),
    r'mk2': (50),
    r'pzschreck': (700, 125),
    r'pzfaust': (400),
    r'deagle': (200, 25),
    r'at4': (450),
    r'rpg7': (600, 100),
    r'glock17': (155, 20),
    r'm1911': (110, 10),
    r'stick': (45),
    r'rgo': (65),
    r'kabar': (70),
    r'm2': (800, 60),
    r'knuckles': (40),
    r'kukri': (90),
    r'aks74u': (235, 30),
    r'g36c': (250, 30),
    r'c96carb': (185, 30),
    r'm4a1': (245, 30),
    r'rpk': (485, 75),
    r'm1a1para': (260, 20),
    r'mk18': (220, 30),
    r'lewis': (400, 55),
    r'm60': (540, 100),
    r'pkm': (950, 200),
    r'sks': (270, 25),
    r'm249': (700, 130),
    r'mg34': (445, 40),
    r'mg42': (1000, 200),
}


def parseFields(lines: list[str]) -> dict[str, str|int]:
    fieldsInfo = {}
    typeCasts = {
        "int": int,
        "uint": int,
        "float": float,
        "string": str,
        "Vector": lambda x, y, z: (float(x), float(y), float(z))
    }
    for line in lines.split('\n'):
        if 'Vector' in line:
            match = re.search(r'(\w+)\(([^<>]*)\)', line)
            fname = match.group(1)
            fxyz = match.group(2).strip().replace('f', '').split(', ')
            fvalue = typeCasts['Vector'](*fxyz)
        else:
            ftypeAndName, fvalueDirty = line.split('=')
            ftype, fnameDirty = ftypeAndName.split(' ')[:2]
            fname = fnameDirty.strip()
            fvalue = fvalueDirty.strip().split(';')[0].replace('"', '').replace('f', '')

            if 'MAX_CLIP' in fvalue:
                fvalue = eval(fvalue.replace('MAX_CLIP', str(fieldsInfo['MAX_CLIP'])))
            elif len(fvalue) > 0 and not fvalue[0].isdigit():
                pass
            else:
                fvalue = typeCasts[ftype](fvalue)

        fieldsInfo[fname] = fvalue

    return fieldsInfo


def parseFile(filePath: str, skipBuyMenuInfo=False) -> dict[str, dict[str, str|int]]:
    weaponInfo = {}
    with open(rf'{filePath}', 'r') as f:
        text = f.read()

    infoText = re.search(r'(?<=\/\/ Information\n)(.+\n)+', text).group(0).strip()
    weaponInfo['infoBasic'] = parseFields(infoText)

    if not skipBuyMenuInfo:
        buyMenuInfoText = re.search(r'(?<=\/\/Buy Menu Information\n)(.+\n)+', text).group(0).strip()
        weaponInfo['infoBuy'] = parseFields(buyMenuInfoText)

    return weaponInfo


if __name__ == '__main__':
    # CS 1.6 part
    weapons16 = {}
    for file in files16:
        weapon = file.split('_')[1][:-3]
        weapons16[weapon] = parseFile(rf'{FILES16_ROOT}\{file}')

    with open('cs16.json', 'w') as f:
        f.write(json.dumps(weapons16, indent=4))

    # Ins part
    weaponsIns = {}
    for file in filesIns:
        weapon = file.split('_ins2')[1][:-3]
        weaponsIns[weapon] = parseFile(rf'{FILES_INS_ROOT}\{file}', True)

        wCost = insCost[weapon]
        wInfo = weaponsIns[weapon]['infoBasic']

        if isinstance(wCost, int):
            wInfo['PRICE'] = wCost
        elif len(wCost) >= 2:
            wInfo['PRICE'] = wCost[0]
            wInfo['PRICE_AMMO'] = wCost[1]
            if len(wCost) == 3:
                wInfo['PRICE_AMMO_GL'] = wCost[2]


    with open('ins.json', 'w') as f:
        f.write(json.dumps(weaponsIns, indent=4))

