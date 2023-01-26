import random

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
