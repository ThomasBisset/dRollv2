from functions import roll


def height_weight_calculator(race):
    match race:
        case "human":
            base_height = 48 + 8
            base_weight = 110
            height = base_height + sum(roll(10, 2))
            weight = base_weight + sum(roll(4, 2))
        case "hill dwarf":
            base_height = 36 + 8
            base_weight = 115
            height = base_height + sum(roll(4, 2))
            weight = base_weight + sum(roll(6, 2))
        case "mountain dwarf":
            base_height = 48
            base_weight = 130
            height = base_height + sum(roll(4, 2))
            weight = base_weight + sum(roll(6, 2))
        case "high elf":
            base_height = 48 + 6
            base_weight = 90
            height = base_height + sum(roll(10, 2))
            weight = base_weight + sum(roll(4, 1))
        case "wood elf":
            base_height = 48 + 6
            base_weight = 100
            height = base_height + sum(roll(10, 2))
            weight = base_weight + sum(roll(4, 1))
        case "drow elf":
            base_height = 48 + 5
            base_weight = 75
            height = base_height + sum(roll(6, 2))
            weight = base_weight + sum(roll(6, 1))
        case "halfling":
            base_height = 24 + 7
            base_weight = 35
            height = base_height + sum(roll(4, 2))
            weight = base_weight
        case "dragonborn":
            base_height = 60
            base_weight = 175
            height = base_height + sum(roll(8, 2))
            weight = base_weight + sum(roll(6, 2))
        case "gnome":
            base_height = 24 + 11
            base_weight = 35
            height = base_height + sum(roll(4, 2))
            weight = base_weight
        case "half-elf":
            base_height = 48 + 9
            base_weight = 110
            height = base_height + sum(roll(8, 2))
            weight = base_weight + sum(roll(4, 2))
        case "half-orc":
            base_height = 48 + 10
            base_weight = 140
            height = base_height + sum(roll(10, 2))
            weight = base_weight + sum(roll(6, 2))
        case "tiefling":
            base_height = 48 + 9
            base_weight = 110
            height = base_height + sum(roll(8, 2))
            weight = base_weight + sum(roll(4, 1))
        case _:
            base_height = 48 + 8
            base_weight = 110
            height = base_height + sum(roll(10, 2))
            weight = base_weight + sum(roll(4, 2))
    return height, weight

