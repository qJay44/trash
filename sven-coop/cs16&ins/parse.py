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
        weapon = file.split('\\')[1][:-3]
        weapons16[weapon] = parseFile(rf'{FILES16_ROOT}\{file}')

    with open('cs16.json', 'w') as f:
        f.write(json.dumps(weapons16, indent=4))

    # Ins part
    weaponsIns = {}
    for file in filesIns:
        weapon = file.split('\\')[1][:-3]
        weaponsIns[weapon] = parseFile(rf'{FILES_INS_ROOT}\{file}', True)

    with open('ins.json', 'w') as f:
        f.write(json.dumps(weaponsIns, indent=4))

