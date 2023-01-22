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


def name_generator(race, gender, **kwargs):
    match race:
        case "dragonborn" | "dwarf" | "elf" | "halfling":
            with open(fr"names\{race}\{gender}.txt") as file:
                name_list = file.read().splitlines()
                first_name = random.choice(name_list).strip()
            with open(fr"names\{race}\surname.txt") as file:
                name_list = file.read().splitlines()
                second_name = random.choice(name_list).strip()
            output = f"{first_name} {second_name}"
            return output
        case "human":
            variant = kwargs["variant"]
            with open(fr"names\{race}\{variant}\{gender}.txt") as file:
                name_list = file.read().splitlines()
                first_name = random.choice(name_list).strip()
            with open(fr"names\{race}\{variant}\surname.txt") as file:
                name_list = file.read().splitlines()
                second_name = random.choice(name_list).strip()
            output = f"{first_name} {second_name}"
            return output
        case "orc" | "tiefling":
            with open(fr"names\{race}\{gender}.txt") as file:
                name_list = file.read().splitlines()
                first_name = random.choice(name_list).strip()
            output = f"{first_name}"
            return output
        case "gnome":
            with open(fr"names\{race}\{gender}.txt") as file:
                name_list = file.read().splitlines()
                first_name = random.choice(name_list).strip()
            with open(fr"names\{race}\nickname.txt") as file:
                name_list = file.read().splitlines()
                nick_name = random.choice(name_list).strip()
            with open(fr"names\{race}\surname.txt") as file:
                name_list = file.read().splitlines()
                second_name = random.choice(name_list).strip()
            gnome_nickname = kwargs["gnome_nickname"]
            if gnome_nickname == 1:
                output = f"{first_name} \"{nick_name}\" {second_name}"
            else:
                output = f"{first_name} {second_name}"
            return output
