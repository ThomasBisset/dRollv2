import random


def criminal_background():
    criminal_speciality = [
        "Blackmailer",
        "Burglar",
        "Enforcer",
        "Fence",
        "Highway robber",
        "Hired killer",
        "Pickpocket",
        "Smuggler"
    ]

    criminal_personality_trait = [
        "I always have a plan for what to do when things go wrong.",
        "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "The first thing I do in a new place is note the location of everything valuable - or where things could be "
        "hidden.",
        "I would rather make a new friend than a new enemy.",
        "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "I don't pay attention to the risks in a situation. Never tell me the odds.",
        "The best way to get me to do something is to tell me I can't do it.",
        "I blow up at the slightest insult."
    ]

    criminal_ideal = [
        "Honor. I don't steal from others in the trade. (Lawful).",
        "Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic).",
        "Charity. I steal from the wealthy so than I can help people in need. (Good).",
        "Greed. I will do whatever it takes to become wealthy. (Evil).",
        "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I "
        "care. (Neutral).",
        "Redemption. There's a spark of good in everyone. (Good)."
    ]

    criminal_bond = [
        "I'm trying to pay off an old debt I owe to a generous benefactor.",
        "My ill-gotten gains go to support my family.",
        "Something important was taken from me, and I aim to steal it back.",
        "I will become the greatest thief that ever lived.",
        "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "Someone I l;oved died because of a mistake I made. That will never happen again."
    ]

    criminal_flaw = [
        "When I see something valuable, I can't think about anything but how to steal it.",
        "When faced with a choice between money and my friends, I usually choose the money.",
        "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "I have a 'tell' that reveals when I'm lying.",
        "I turn tail and run when things look bad.",
        "An innocent person is in prison for a crime I committed. I'm okay with that."
    ]

    specialty = random.choice(criminal_speciality)
    personality_trait = random.choice(criminal_personality_trait)
    ideal = random.choice(criminal_ideal)
    bond = random.choice(criminal_bond)
    flaw = random.choice(criminal_flaw)

    return personality_trait, ideal, bond, flaw, specialty
