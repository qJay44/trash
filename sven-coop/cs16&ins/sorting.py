import json

def sort(e):
    return e['infoBasic'].get('DAMAGE', -1)

with open('cs16.json', 'r') as f:
    data = json.loads(f.read())

    weapons = [v for v in data.values()]
    weapons.sort(key=sort)
    print(json.dumps(weapons, indent=4))
