import math
import random

from functions import name_generator, ability_generator
from backgrounds.acolyte import acolyte_background
from backgrounds.charlatan import charlatan_background
from backgrounds.criminal import criminal_background
from backgrounds.entertainer import entertainer_background
from backgrounds.folk_hero import folk_hero_background
from backgrounds.guild_artisan import guild_artisan_background
from backgrounds.hermit import hermit_background
from backgrounds.noble import noble_background
from backgrounds.outlander import outlander_background
from backgrounds.sage import sage_background
from backgrounds.sailor import sailor_background
from backgrounds.soldier import soldier_background
from backgrounds.urchin import urchin_background

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

match character["Background"]:
    case "acolyte":
        character["Personality Trait"] = acolyte_background()[0]
        character["Ideal"] = acolyte_background()[1]
        character["Bond"] = acolyte_background()[2]
        character["Flaw"] = acolyte_background()[3]
    case "charlatan":
        character["Personality Trait"] = charlatan_background()[0]
        character["Ideal"] = charlatan_background()[1]
        character["Bond"] = charlatan_background()[2]
        character["Flaw"] = charlatan_background()[3]
        character["Scam"] = charlatan_background()[4]
    case "criminal":
        character["Personality Trait"] = criminal_background()[0]
        character["Ideal"] = criminal_background()[1]
        character["Bond"] = criminal_background()[2]
        character["Flaw"] = criminal_background()[3]
        character["Speciality"] = criminal_background()[4]
    case "entertainer":
        character["Personality Trait"] = entertainer_background()[0]
        character["Ideal"] = entertainer_background()[1]
        character["Bond"] = entertainer_background()[2]
        character["Flaw"] = entertainer_background()[3]
        character["Routine"] = entertainer_background()[4]
    case "folk hero":
        character["Personality Trait"] = folk_hero_background()[0]
        character["Ideal"] = folk_hero_background()[1]
        character["Bond"] = folk_hero_background()[2]
        character["Flaw"] = folk_hero_background()[3]
        character["Defining Event"] = folk_hero_background()[4]
    case "guild artisan":
        character["Personality Trait"] = guild_artisan_background()[0]
        character["Ideal"] = guild_artisan_background()[1]
        character["Bond"] = guild_artisan_background()[2]
        character["Flaw"] = guild_artisan_background()[3]
        character["Guild Business"] = guild_artisan_background()[4]
    case "hermit":
        character["Personality Trait"] = hermit_background()[0]
        character["Ideal"] = hermit_background()[1]
        character["Bond"] = hermit_background()[2]
        character["Flaw"] = hermit_background()[3]
        character["Life of Seclusion"] = hermit_background()[4]
    case "noble":
        character["Personality Trait"] = noble_background()[0]
        character["Ideal"] = noble_background()[1]
        character["Bond"] = noble_background()[2]
        character["Flaw"] = noble_background()[3]
    case "outlander":
        character["Personality Trait"] = outlander_background()[0]
        character["Ideal"] = outlander_background()[1]
        character["Bond"] = outlander_background()[2]
        character["Flaw"] = outlander_background()[3]
        character["Origin"] = outlander_background()[4]
    case "sage":
        character["Personality Trait"] = sage_background()[0]
        character["Ideal"] = sage_background()[1]
        character["Bond"] = sage_background()[2]
        character["Flaw"] = sage_background()[3]
        character["Speciality"] = sage_background()[4]
    case "sailor":
        character["Personality Trait"] = sailor_background()[0]
        character["Ideal"] = sailor_background()[1]
        character["Bond"] = sailor_background()[2]
        character["Flaw"] = sailor_background()[3]
    case "soldier":
        character["Personality Trait"] = soldier_background()[0]
        character["Ideal"] = soldier_background()[1]
        character["Bond"] = soldier_background()[2]
        character["Flaw"] = soldier_background()[3]
        character["Speciality"] = soldier_background()[4]
    case "urchin":
        character["Personality Trait"] = urchin_background()[0]
        character["Ideal"] = urchin_background()[1]
        character["Bond"] = urchin_background()[2]
        character["Flaw"] = urchin_background()[3]

print()
print(f" |------------------------------| ")
print(f" |     DUNGEONS AND DRAGONS     | ")
print(f" |   Random Character Creator   | ")
print(f" |------------------------------| ")
print()
print(f"NAME:                {character['Name']} ({character['Gender'].title()})")
print(f"RACE AND CLASS:      {character['Race'].title()}, {character['Character Class'].title()} "
      f"{character['Background'].title()}")
print()
print(f"STR: {character['STR']: <2} ({character['STR Mod']:+g})")
print(f"DEX: {character['DEX']: <2} ({character['DEX Mod']:+g})")
print(f"CON: {character['CON']: <2} ({character['CON Mod']:+g})")
print(f"INT: {character['INT']: <2} ({character['INT Mod']:+g})")
print(f"WIS: {character['WIS']: <2} ({character['WIS Mod']:+g})")
print(f"CHA: {character['CHA']: <2} ({character['CHA Mod']:+g})")
print()
print(f"Personality Trait:   {character['Personality Trait']}")
print(f"Ideal:               {character['Ideal']}")
print(f"Bond:                {character['Bond']}")
print(f"Flaw:                {character['Flaw']}")
