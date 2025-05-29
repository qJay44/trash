import pickle
from random import choice

def init():
    with open('kz_maps.txt', 'r') as f:
        maps = f.readlines()

    return choose(maps)


def choose(maps):
    map = choice(maps)
    maps.remove(map)
    with open('kz_maps_cycle.pkl', 'wb') as f:
        pickle.dump(maps, f)

    return map


def cycle():
    with open('kz_maps_cycle.pkl', 'rb') as f:
        maps = pickle.load(f)

    if len(maps) == 0:
        return init()

    return choose(maps)


if __name__ == '__main__':
    try:
        print(cycle())
    except FileNotFoundError:
        print(init())

