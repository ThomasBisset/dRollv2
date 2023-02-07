from random_character import random_character
from functions import height_conversion_ft_in


if __name__ == "__main__":
    character = random_character()

    print()
    print(f">>>>> D&D Random Character >>>>>")
    print()

    print(f"{character['Name'].title()} "
          f"({character['Gender']}); the "
          f"{character['Race'].title()}, "
          f"{character['Background'].title()} "
          f"{character['Character Class'].title()}")

    print(f"Height: {height_conversion_ft_in(character['Height'])}  |  "
          f"Weight: {character['Weight']}lbs")

    print()

    print(f"STR: {character['STR']} ({character['STR Mod']})  |  "
          f"DEX: {character['DEX']} ({character['DEX Mod']})  |  "
          f"CON: {character['CON']} ({character['CON Mod']})  |  "
          f"INT: {character['INT']} ({character['INT Mod']})  |  "
          f"WIS: {character['WIS']} ({character['WIS Mod']})  |  "
          f"CHA: {character['CHA']} ({character['CHA Mod']})")

    print()

    print(f"Personality Trait:  {character['Personality Trait']}")
    print(f"Ideal:              {character['Ideal']}")
    print(f"Bond:               {character['Bond']}")
    print(f"Flaw:               {character['Flaw']}")

    match character['Character Class']:
        case "barbarian":
            print(f'Totem:              {character["Totem"]}')
            print(f'Tattoo:             {character["Tattoo"]}')
            print(f'Superstition:       {character["Superstition"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "bard":
            print(f'Defining Work:      {character["Defining Work"]}')
            print(f'Instrument:         {character["Instrument"]}')
            print(f'Embarrassment:      {character["Embarrassment"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "cleric":
            print(f'Temple:             {character["Temple"]}')
            print(f'Keepsake:           {character["Keepsake"]}')
            print(f'Secret:             {character["Secret"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "druid":
            print(f'Treasured Item:     {character["Treasured Item"]}')
            print(f'Guiding Aspect:     {character["Guiding Aspect"]}')
            print(f'Mentor:             {character["Mentor"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "fighter":
            print(f'Heraldic Sign:      {character["Heraldic Sign"]}')
            print(f'Instructor:         {character["Instructor"]}')
            print(f'Signature Style:    {character["Signature Style"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "monk":
            print(f'Monastery:          {character["Monastery"]}')
            print(f'Monastic Icons:     {character["Monastic Icons"]}')
            print(f'Monk Master:        {character["Monk Master"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "paladin":
            print(f'Personal Goal:      {character["Personal Goal"]}')
            print(f'Symbol:             {character["Symbol"]}')
            print(f'Nemesis:            {character["Nemesis"]}')
            print(f'Temptation:         {character["Temptation"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "ranger":
            print(f'View of the World:  {character["View of the World"]}')
            print(f'Homeland:           {character["Homeland"]}')
            print(f'Sworn Enemy:        {character["Sworn Enemy"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "rogue":
            print(f'Guilty Pleasure:    {character["Guilty Pleasure"]}')
            print(f'Adversary:          {character["Adversary"]}')
            print(f'Benefactor:         {character["Benefactor"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "sorcerer":
            print(f'Arcane Origin:      {character["Arcane Origin"]}')
            print(f'Reactions:          {character["Reactions"]}')
            print(f'Supernatural Mark:  {character["Supernatural Mark"]}')
            print(f'Signs of Sorcery:   {character["Signs of Sorcery"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "warlock":
            print(f'Patron Attitude:    {character["Patron Attitude"]}')
            print(f'Special Terms:      {character["Special Terms"]}')
            print(f'Binding Mark:       {character["Binding Mark"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case "wizard":
            print(f'Spellbook:          {character["Spellbook"]}')
            print(f'Ambition:           {character["Ambition"]}')
            print(f'Eccentricity:       {character["Eccentricity"]}')
            print(f'Reason for Being:   {character["Reason for Being"]}')
        case _:
            pass

    match character["Background"]:
        case "charlatan":
            print(f'Scam:               {character["Scam"]}')
        case "criminal" | "sage" | "soldier":
            print(f'Speciality:         {character["Speciality"]}')
        case "entertainer":
            print(f'Routine:            {character["Routine"]}')
        case "folk hero":
            print(f'Defining Event:     {character["Defining Event"]}')
        case "guild artisan":
            print(f'Guild Business:     {character["Guild Business"]}')
        case "hermit":
            print(f'Life of Seclusion:  {character["Life of Seclusion"]}')
        case "outlander":
            print(f'Origin:             {character["Origin"]}')
