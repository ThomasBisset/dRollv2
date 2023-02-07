import random
import math


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
    for i in range(6):
        abilities_list.append(sum(ability_roll()))
        abilities_list.sort(reverse=True)
    return abilities_list


def modifier_calculator(ability):
    modifier = math.floor((ability - 10) / 2)
    return modifier


def height_conversion_ft_in(height_in):
    inches = height_in % 12
    feet = (height_in - inches) / 12
    output = f"{int(feet)}ft {int(inches)}in"
    return output
