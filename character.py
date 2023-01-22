import math
import random

from functions import name_generator, ability_generator

character = {}

race_list = ["dwarf", "elf", "halfling", "human", "dragonborn", "gnome", "half-elf", "half-orc", "tiefling"]
dwarf_variants = ["hill", "mountain"]
elf_variants = ["high", "wood", "drow"]
halfling_variants = ["lightfoot", "stout"]
human_variants = ["calashite", "chondathan", "damaran", "illuskan", "mulan", "rashemi", "shou", "tethyrian", "turami"]
dragonborn_variants = ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"]
gnome_variants = ["forest", "rock"]

character["Race"] = random.choice(race_list)

match character["Race"]:
    case "dwarf":
        variant = random.choice(dwarf_variants)
        character['Race'] = f"{variant} {character['Race']}"
        character['Gender'] = random.choice(["male", "female"])
        character['Name'] = name_generator("dwarf", character['Gender'])
    case "elf":
        variant = random.choice(elf_variants)
        character['Race'] = f"{variant} {character['Race']}"
        character['Gender'] = random.choice(["male", "female", "child"])
        character['Name'] = name_generator("elf", character['Gender'])
    case "halfling":
        variant = random.choice(halfling_variants)
        character['Race'] = f"{variant} {character['Race']}"
        character['Gender'] = random.choice(["male", "female"])
        character['Name'] = name_generator("halfling", character['Gender'])
    case "human":
        variant = random.choice(human_variants)
        character['Race'] = f"{variant} {character['Race']}"
        character['Gender'] = random.choice(["male", "female"])
        if variant == "chondathan" or variant == "tethyrian":
            name_variant = "chondathan_tethyrian"
        else:
            name_variant = variant
        character['Name'] = name_generator("human", character['Gender'], variant=name_variant)
    case "dragonborn":
        variant = random.choice(dragonborn_variants)
        character['Race'] = f"{variant} {character['Race']}"
        character['Gender'] = random.choice(["male", "female", "child"])
        character['Name'] = name_generator("dragonborn", character['Gender'])
    case "gnome":
        variant = random.choice(gnome_variants)
        character['Race'] = f"{variant} {character['Race']}"
        character['Gender'] = random.choice(["male", "female"])
        nickname = random.choice([0, 1])
        character['Name'] = name_generator("gnome", character['Gender'], gnome_nickname=nickname)
    case "half-elf":
        human_or_elf = random.choice(["human", "elf"])
        if human_or_elf == "human":
            variant = random.choice(human_variants)
            character['Gender'] = random.choice(["male", "female"])
            if variant == "chondathan" or variant == "tethyrian":
                name_variant = "chondathan_tethyrian"
            else:
                name_variant = variant
            character['Name'] = name_generator("human", character['Gender'], variant=name_variant)
        elif human_or_elf == "elf":
            character['Gender'] = random.choice(["male", "female", "child"])
            character['Name'] = name_generator("elf", character['Gender'])
    case "half-orc":
        character['Gender'] = random.choice(["male", "female"])
        character['Name'] = name_generator("orc", character['Gender'])
    case "tiefling":
        character['Gender'] = random.choice(["male", "female", "virtue"])
        character['Name'] = name_generator("tiefling", character['Gender'])
        if character['Gender'] == "virtue":
            gender = "neutral"
    case _:
        character['Gender'] = "neutral"
        character['Name'] = "unknown"

character_class_list = ["artificer", "barbarian", "bard", "cleric", "druid", "fighter", "monk",
                        "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

background_list = ["acolyte", "charlatan", "criminal", "entertainer", "folk hero", "guild artisan",
                   "hermit", "noble", "outlander", "sage", "sailor", "soldier", "urchin"]

character["Character Class"] = random.choice(character_class_list)
character["Background"] = random.choice(background_list)

ability_roll = ability_generator()

match character["Character Class"]:
    case "artificer":
        character["INT"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["DEX"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["STR"] = ability_roll[4]
        character["CHA"] = ability_roll[5]
    case "barbarian":
        character["STR"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["DEX"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["CHA"] = ability_roll[4]
        character["INT"] = ability_roll[5]
    case "bard":
        character["CHA"] = ability_roll[0]
        character["DEX"] = ability_roll[1]
        character["CON"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["INT"] = ability_roll[4]
        character["STR"] = ability_roll[5]
    case "cleric":
        character["WIS"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["STR"] = ability_roll[2]
        character["DEX"] = ability_roll[3]
        character["CHA"] = ability_roll[4]
        character["INT"] = ability_roll[5]
    case "druid":
        character["WIS"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["DEX"] = ability_roll[2]
        character["CHA"] = ability_roll[3]
        character["INT"] = ability_roll[4]
        character["STR"] = ability_roll[5]
    case "fighter":
        character["STR"] = ability_roll[0]
        character["DEX"] = ability_roll[1]
        character["CON"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["CHA"] = ability_roll[4]
        character["INT"] = ability_roll[5]
    case "monk":
        character["DEX"] = ability_roll[0]
        character["WIS"] = ability_roll[1]
        character["CON"] = ability_roll[2]
        character["CHA"] = ability_roll[3]
        character["STR"] = ability_roll[4]
        character["INT"] = ability_roll[5]
    case "paladin":
        character["STR"] = ability_roll[0]
        character["CHA"] = ability_roll[1]
        character["CON"] = ability_roll[2]
        character["DEX"] = ability_roll[3]
        character["WIS"] = ability_roll[4]
        character["INT"] = ability_roll[5]
    case "ranger":
        character["DEX"] = ability_roll[0]
        character["WIS"] = ability_roll[1]
        character["CON"] = ability_roll[2]
        character["STR"] = ability_roll[3]
        character["CHA"] = ability_roll[4]
        character["INT"] = ability_roll[5]
    case "barbarian":
        character["DEX"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["WIS"] = ability_roll[2]
        character["CHA"] = ability_roll[3]
        character["INT"] = ability_roll[4]
        character["STR"] = ability_roll[5]
    case "sorcerer":
        character["CHA"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["DEX"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["INT"] = ability_roll[4]
        character["STR"] = ability_roll[5]
    case "warlock":
        character["CHA"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["DEX"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["INT"] = ability_roll[4]
        character["STR"] = ability_roll[5]
    case "wizard":
        character["INT"] = ability_roll[0]
        character["CON"] = ability_roll[1]
        character["DEX"] = ability_roll[2]
        character["WIS"] = ability_roll[3]
        character["CHA"] = ability_roll[4]
        character["STR"] = ability_roll[5]
    case _:
        character["CON"] = ability_roll[0]
        character["DEX"] = ability_roll[1]
        character["WIS"] = ability_roll[2]
        character["CHA"] = ability_roll[3]
        character["STR"] = ability_roll[4]
        character["INT"] = ability_roll[5]

character["STR Mod"] = math.floor((character["STR"] - 10) / 2)
character["DEX Mod"] = math.floor((character["DEX"] - 10) / 2)
character["CON Mod"] = math.floor((character["CON"] - 10) / 2)
character["INT Mod"] = math.floor((character["INT"] - 10) / 2)
character["WIS Mod"] = math.floor((character["WIS"] - 10) / 2)
character["CHA Mod"] = math.floor((character["CHA"] - 10) / 2)

print(f"{character['Name']} ({character['Gender'].title()})")
print(f"{character['Race'].title()}, {character['Character Class'].title()} {character['Background'].title()}")
print(f"STR: {character['STR']: <2} ({character['STR Mod']:+g})")
print(f"DEX: {character['DEX']: <2} ({character['DEX Mod']:+g})")
print(f"CON: {character['CON']: <2} ({character['CON Mod']:+g})")
print(f"INT: {character['INT']: <2} ({character['INT Mod']:+g})")
print(f"WIS: {character['WIS']: <2} ({character['WIS Mod']:+g})")
print(f"CHA: {character['CHA']: <2} ({character['CHA Mod']:+g})")
