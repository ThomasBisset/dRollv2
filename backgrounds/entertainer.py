# proficiency: acrobatics, performance

import random


def entertainer_background():
    entertainer_routines = [
        "Actor",
        "Dancer",
        "Fire-eater",
        "Jester",
        "Juggler",
        "Instrumentalist",
        "Poet",
        "Singer",
        "Storyteller",
        "Tumbler"
    ]

    entertainer_personality_trait = [
        "I know a story relevant to almost every situation.",
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I'm a hopeless romantic, always searching for that 'special someone'.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I love a good insult, even one directed at me.",
        "I get bitter if I'm not the centre of attention.",
        "I'll settle for nothing less than perfection.",
        "I change my mood or my mind as quickly as I change key in a song."
    ]

    entertainer_ideal = [
        "Beauty. When I perform, I make the world better than it was. (Good).",
        "Tradition. The stories, legends and songs of the past must never be forgotten, for they teach us who we are. "
        "(Lawful).",
        "Creativity. The world is in need of new ideas and bold action. (Chaotic).",
        "Greed. I'm only in it for the money and fame. (Evil).",
        "People. I like seeing the smiles on people's faces when I perform. That's all that matters. (Neutral).",
        "Honesty. Art should reflect the soul; it should come from within and reveal who we really are. (Any)."
    ]

    entertainer_bond = [
        "My instrument is my most treasured possession, and it reminds me of someone I love.",
        "Someone stole my precious instrument, and someday I'll get it back.",
        "I want to be famous, whatever it takes.",
        "I idolize a hero of the old tales and measure my deeds against a person's.",
        "I will do any thing to prove myself superior to my hated rival.",
        "I would do anything for the other members of my old troupe."
    ]

    entertainer_flaw = [
        "I'll do anything to win fame and renown.",
        "I'm a sucker for a pretty face.",
        "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
        "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
        "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
        "Despite my best efforts, I am unreliable to my friends."
    ]

    routine = random.choice(entertainer_routines)
    personality_trait = random.choice(entertainer_personality_trait)
    ideal = random.choice(entertainer_ideal)
    bond = random.choice(entertainer_bond)
    flaw = random.choice(entertainer_flaw)

    return personality_trait, ideal, bond, flaw, routine
