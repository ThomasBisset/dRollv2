# proficiency: medicine, religion

import random


def hermit_background():
    hermit_life_of_seclusion = [
        "I was searching for spiritual enlightenment.",
        "I was partaking of communal living in accordance with the dictates of a religious order.",
        "I was exiled for a crime I didn't commit.",
        "I retreated from society after a life-altering event.",
        "I needed a quiet place to work on my art, literature, music, or manifesto.",
        "I needed to commune with nature, far from civilization.",
        "I was the caretaker of an ancient ruin or relic.",
        "I was a pilgrim in search of a person, place, or relic of spiritual significance."
    ]

    hermit_personality_traits = [
        "I've been isolated for so long that I rarely speak, preferring gestures and the occasional "
        "grunt.",
        "I am utterly serene, even in the face of disaster.",
        "The leader of my community had something wise to say on every topic, and I am eager to share "
        "that wisdom.",
        "I feel tremendous empathy for all who suffer.",
        "I'm oblivious to etiquette and social expectations.",
        "I connect everything that happens to me to a grand, cosmic plan.",
        "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
        "I am working on a grand philosophical theory and love sharing my ideas."
    ]

    hermit_ideals = [
        "Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)",
        "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking. "
        "(Lawful)",
        "Free Thinking. Inquiry and curiosity are the pillars of progress. (Chaotic)",
        "Power. Solitude and contemplation are paths toward mystical or magical power. (Evil)",
        "Live and Let Live. Meddling in the affairs of others only causes trouble. (Neutral)",
        "Self-Knowledge. If you know yourself, there's nothing left to know. (Any)"
    ]

    hermit_bonds = [
        "Nothing is more important than the other members of my hermitage, order, or association.",
        "I entered seclusion to hide from the ones who might still be hunting me. I must someday "
        "confront them.",
        "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
        "I entered seclusion because I loved someone I could not have.",
        "Should my discovery come to light, it could bring ruin to the world.",
        "My isolation gave me great insight into a great evil that only I can destroy."
    ]

    hermit_flaw = [
        "Now that I've returned to the world, I enjoy its delights a little too much.",
        "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.",
        "I am dogmatic in my thoughts and philosophy.",
        "I let my need to win arguments overshadow friendships and harmony.",
        "I'd risk too much to uncover a lost bit of knowledge.",
        "I like keeping secrets and won't share them with anyone."
    ]

    life_of_seclusion = random.choice(hermit_life_of_seclusion)
    personality_trait = random.choice(hermit_personality_traits)
    ideal = random.choice(hermit_ideals)
    bond = random.choice(hermit_bonds)
    flaw = random.choice(hermit_flaw)

    return personality_trait, ideal, bond, flaw, life_of_seclusion
