import random

from functions import ability_generator, modifier_calculator, height_weight_calculator
from name_generator import name_generator
from backgrounds import acolyte_background, charlatan_background, criminal_background, entertainer_background, \
    folk_hero_background, guild_artisan_background, hermit_background, noble_background, outlander_background, \
    sage_background, sailor_background, soldier_background, urchin_background
from xanathars import barbarian_xgte, bard_xgte, cleric_xgte, druid_xgte, fighter_xgte, monk_xgte, ranger_xgte, \
    rogue_xgte, paladin_xgte, sorcerer_xgte, warlock_xgte, wizard_xgte


def random_character():
    character = {}

    race_list = ["dwarf", "elf", "halfling", "human", "dragonborn",
                 "gnome", "half-elf", "half-orc", "tiefling"]

    dwarf_variants = ["hill", "mountain"]
    elf_variants = ["high", "wood", "drow"]
    halfling_variants = ["lightfoot", "stout"]
    human_variants = ["calashite", "chondathan", "damaran", "illuskan", "mulan",
                      "rashemi", "shou", "tethyrian", "turami"]
    dragonborn_variants = ["black", "blue", "brass", "bronze", "copper",
                           "gold", "green", "red", "silver", "white"]
    gnome_variants = ["forest", "rock"]

    character_class_list = ["artificer", "barbarian", "bard", "cleric", "druid", "fighter", "monk",
                            "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

    background_list = ["acolyte", "charlatan", "criminal", "entertainer", "folk hero", "guild artisan",
                       "hermit", "noble", "outlander", "sage", "sailor", "soldier", "urchin"]

    ability_roll = ability_generator()

    character["Race"] = random.choice(race_list)
    character["Character Class"] = random.choice(character_class_list)
    character["Background"] = random.choice(background_list)

    match character["Race"]:
        case "dwarf":
            variant = random.choice(dwarf_variants)
            character['Race'] = f"{variant} {character['Race']}"
            character['Gender'] = random.choice(["male", "female"])
            character['Name'] = name_generator("dwarf", character['Gender'])
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
        case "elf":
            variant = random.choice(elf_variants)
            character['Race'] = f"{variant} {character['Race']}"
            character['Gender'] = random.choice(["male", "female", "child"])
            character['Name'] = name_generator("elf", character['Gender'])
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
        case "halfling":
            variant = random.choice(halfling_variants)
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
            character['Race'] = f"{variant} {character['Race']}"
            character['Gender'] = random.choice(["male", "female"])
            character['Name'] = name_generator("halfling", character['Gender'])
        case "human":
            variant = random.choice(human_variants)
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
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
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
        case "gnome":
            variant = random.choice(gnome_variants)
            character['Race'] = f"{variant} {character['Race']}"
            character['Gender'] = random.choice(["male", "female"])
            nickname = random.choice([0, 1])
            character['Name'] = name_generator("gnome", character['Gender'], gnome_nickname=nickname)
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
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
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
        case "half-orc":
            character['Gender'] = random.choice(["male", "female"])
            character['Name'] = name_generator("orc", character['Gender'])
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
        case "tiefling":
            character['Gender'] = random.choice(["male", "female", "virtue"])
            character['Name'] = name_generator("tiefling", character['Gender'])
            if character['Gender'] == "virtue":
                character["Gender"] = "neutral"
            character['Height'] = height_weight_calculator(character['Race'])[0]
            character['Weight'] = height_weight_calculator(character['Race'])[1]
        case _:
            print("Error")
            exit()

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
            character["Totem"] = barbarian_xgte()[0]
            character["Tattoo"] = barbarian_xgte()[1]
            character["Superstition"] = barbarian_xgte()[2]
            character["Reason for Being"] = barbarian_xgte()[3]
        case "bard":
            character["CHA"] = ability_roll[0]
            character["DEX"] = ability_roll[1]
            character["CON"] = ability_roll[2]
            character["WIS"] = ability_roll[3]
            character["INT"] = ability_roll[4]
            character["STR"] = ability_roll[5]
            character["Defining Work"] = bard_xgte()[0]
            character["Instrument"] = bard_xgte()[1]
            character["Embarrassment"] = bard_xgte()[2]
            character["Reason for Being"] = bard_xgte()[3]
        case "cleric":
            character["WIS"] = ability_roll[0]
            character["CON"] = ability_roll[1]
            character["STR"] = ability_roll[2]
            character["DEX"] = ability_roll[3]
            character["CHA"] = ability_roll[4]
            character["INT"] = ability_roll[5]
            character["Temple"] = cleric_xgte()[0]
            character["Keepsake"] = cleric_xgte()[1]
            character["Secret"] = cleric_xgte()[2]
            character["Reason for Being"] = cleric_xgte()[3]
        case "druid":
            character["WIS"] = ability_roll[0]
            character["CON"] = ability_roll[1]
            character["DEX"] = ability_roll[2]
            character["CHA"] = ability_roll[3]
            character["INT"] = ability_roll[4]
            character["STR"] = ability_roll[5]
            character["Treasured Item"] = druid_xgte()[0]
            character["Guiding Aspect"] = druid_xgte()[1]
            character["Mentor"] = druid_xgte()[2]
            character["Reason for Being"] = druid_xgte()[3]
        case "fighter":
            character["STR"] = ability_roll[0]
            character["DEX"] = ability_roll[1]
            character["CON"] = ability_roll[2]
            character["WIS"] = ability_roll[3]
            character["CHA"] = ability_roll[4]
            character["INT"] = ability_roll[5]
            character["Heraldic Sign"] = fighter_xgte()[0]
            character["Instructor"] = fighter_xgte()[1]
            character["Signature Style"] = fighter_xgte()[2]
            character["Reason for Being"] = fighter_xgte()[3]
        case "monk":
            character["DEX"] = ability_roll[0]
            character["WIS"] = ability_roll[1]
            character["CON"] = ability_roll[2]
            character["CHA"] = ability_roll[3]
            character["STR"] = ability_roll[4]
            character["INT"] = ability_roll[5]
            character["Monastery"] = monk_xgte()[0]
            character["Monastic Icons"] = monk_xgte()[1]
            character["Monk Master"] = monk_xgte()[2]
            character["Reason for Being"] = monk_xgte()[3]
        case "paladin":
            character["STR"] = ability_roll[0]
            character["CHA"] = ability_roll[1]
            character["CON"] = ability_roll[2]
            character["DEX"] = ability_roll[3]
            character["WIS"] = ability_roll[4]
            character["INT"] = ability_roll[5]
            character["Personal Goal"] = paladin_xgte()[0]
            character["Symbol"] = paladin_xgte()[1]
            character["Nemesis"] = paladin_xgte()[2]
            character["Temptation"] = paladin_xgte()[3]
            character["Reason for Being"] = paladin_xgte()[4]
        case "ranger":
            character["DEX"] = ability_roll[0]
            character["WIS"] = ability_roll[1]
            character["CON"] = ability_roll[2]
            character["STR"] = ability_roll[3]
            character["CHA"] = ability_roll[4]
            character["INT"] = ability_roll[5]
            character["View of the World"] = ranger_xgte()[0]
            character["Homeland"] = ranger_xgte()[1]
            character["Sworn Enemy"] = ranger_xgte()[2]
            character["Reason for Being"] = ranger_xgte()[3]
        case "rogue":
            character["DEX"] = ability_roll[0]
            character["CON"] = ability_roll[1]
            character["WIS"] = ability_roll[2]
            character["CHA"] = ability_roll[3]
            character["INT"] = ability_roll[4]
            character["STR"] = ability_roll[5]
            character["Guilty Pleasure"] = rogue_xgte()[0]
            character["Adversary"] = rogue_xgte()[1]
            character["Benefactor"] = rogue_xgte()[2]
            character["Reason for Being"] = rogue_xgte()[3]
        case "sorcerer":
            character["CHA"] = ability_roll[0]
            character["CON"] = ability_roll[1]
            character["DEX"] = ability_roll[2]
            character["WIS"] = ability_roll[3]
            character["INT"] = ability_roll[4]
            character["STR"] = ability_roll[5]
            character["Arcane Origin"] = sorcerer_xgte()[0]
            character["Reactions"] = sorcerer_xgte()[1]
            character["Supernatural Mark"] = sorcerer_xgte()[2]
            character["Signs of Sorcery"] = sorcerer_xgte()[3]
            character["Reason for Being"] = sorcerer_xgte()[4]
        case "warlock":
            character["CHA"] = ability_roll[0]
            character["CON"] = ability_roll[1]
            character["DEX"] = ability_roll[2]
            character["WIS"] = ability_roll[3]
            character["INT"] = ability_roll[4]
            character["STR"] = ability_roll[5]
            character["Patron Attitude"] = warlock_xgte()[0]
            character["Special Terms"] = warlock_xgte()[1]
            character["Binding Mark"] = warlock_xgte()[2]
            character["Reason for Being"] = warlock_xgte()[3]
        case "wizard":
            character["INT"] = ability_roll[0]
            character["CON"] = ability_roll[1]
            character["DEX"] = ability_roll[2]
            character["WIS"] = ability_roll[3]
            character["CHA"] = ability_roll[4]
            character["STR"] = ability_roll[5]
            character["Spellbook"] = wizard_xgte()[0]
            character["Ambition"] = wizard_xgte()[1]
            character["Eccentricity"] = wizard_xgte()[2]
            character["Reason for Being"] = wizard_xgte()[3]
        case _:
            print("Error")
            exit()

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

    match character["Race"]:
        case "hill dwarf":
            character["CON"] = character["CON"] + 2
            character["WIS"] = character["WIS"] + 1
        case "mountain dwarf":
            character["CON"] = character["CON"] + 2
            character["STR"] = character["STR"] + 2
        case "high elf":
            character["DEX"] = character["DEX"] + 2
            character["INT"] = character["INT"] + 1
        case "wood elf":
            character["DEX"] = character["DEX"] + 2
            character["WIS"] = character["WIS"] + 1
        case "wood elf":
            character["DEX"] = character["DEX"] + 2
            character["CHA"] = character["CHA"] + 1
        case "lightfoot halfling":
            character["DEX"] = character["DEX"] + 2
            character["CHA"] = character["CHA"] + 1
        case "stout halfling":
            character["DEX"] = character["DEX"] + 2
            character["CON"] = character["CON"] + 1
        case "forest gnome":
            character["INT"] = character["INT"] + 2
            character["DEX"] = character["DEX"] + 1
        case "rock gnome":
            character["INT"] = character["INT"] + 2
            character["CON"] = character["CON"] + 1
        case "half-elf":
            character["CHA"] = character["CHA"] + 2
        case "half-orc":
            character["STR"] = character["STR"] + 2
            character["CON"] = character["CON"] + 1
        case "tiefling":
            character["CHA"] = character["CHA"] + 2
            character["INT"] = character["INT"] + 1
        case _:
            if character["Race"][-5:] == "human":
                character["STR"] = character["STR"] + 1
                character["DEX"] = character["DEX"] + 1
                character["CON"] = character["CON"] + 1
                character["INT"] = character["INT"] + 1
                character["WIS"] = character["WIS"] + 1
                character["CHA"] = character["CHA"] + 1
            elif character["Race"][-10:] == "dragonborn":
                character["STR"] = character["STR"] + 2
                character["CHA"] = character["CHA"] + 1

    character["STR Mod"] = modifier_calculator(character["STR"])
    character["DEX Mod"] = modifier_calculator(character["DEX"])
    character["CON Mod"] = modifier_calculator(character["CON"])
    character["INT Mod"] = modifier_calculator(character["INT"])
    character["WIS Mod"] = modifier_calculator(character["WIS"])
    character["CHA Mod"] = modifier_calculator(character["CHA"])

    return character
