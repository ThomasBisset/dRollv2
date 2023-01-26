import random


def roll(d, x):
    output = []
    loop = 1
    while loop <= x:
        output.append(random.randint(1, d))
        loop = loop + 1
    return output


def ability_roll():
    result = roll(6, 4)
    result.remove(min(result))
    return result


def ability_generator():
    abilities_list = []
    for loop in range(6):
        abilities_list.append(sum(ability_roll()))
        abilities_list.sort(reverse=True)
    return abilities_list
