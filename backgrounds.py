import random


def acolyte_background():
    acolyte_personality_trait = [
        "I idolize a particular hero of my faith, and constantly refer to that person’s deeds and example.",
        "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
        "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
        "Nothing can shake my optimistic attitude.",
        "I quote (or misquote) sacred texts and proverbs in almost every situation.",
        "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
        "I’ve enjoyed fine food, drink, and high society among my temple’s elite. Rough living grates on me.",
        "I’ve spent so long in the temple that I have little practical experience dealing with people in the outside "
        "world."
    ]

    acolyte_ideal = [
        "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)",
        "Charity. I always try to help those in need, no matter what the personal cost. (Good)",
        "Change. We must help bring about the changes the gods are constantly working in the world. (Chaotic)",
        "Power. I hope to one day rise to the top of my faith’s religious hierarchy. (Lawful)",
        "Faith.I trust that my deity will guide my actions.I have faith that if I work hard, things will go well. "
        "(Lawful)",
        "Aspiration. I seek to prove myself worthy of my god’s favor by matching my actions against his or her "
        "teachings. (Any)"
    ]

    acolyte_bond = [
        "I would die to recover an ancient relic of my faith that was lost long ago.",
        "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        "I owe my life to the priest who took me in when my parents died.",
        "Everything I do is for the common people.",
        "I will do anything to protect the temple where I served.",
        "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy."
    ]

    acolyte_flaw = [
        "I judge others harshly, and myself even more severely.",
        "I put too much trust in those who wield power within my temple’s hierarchy.",
        "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "I am inflexible in my thinking.",
        "I am suspicious of strangers and expect the worst of them.",
        "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
    ]

    acolyte_origin_xgte = [
        "I ran away from home at an early age and found refuge in a temple.",
        "My family gave me to a temple, since they were unable or unwilling to care for me.",
        "I grew up in a household with strong religious convictions. Entering the service of one or more gods seemed "
        "natural.",
        "An impassioned sermon struck a chord deep in my soul and moved me to serve the faith.",
        "I followed a childhood friend, a respected acquaintance, or someone I loved into religious service.",
        "After encountering a true servant of the gods, I was so inspired that I immediately entered the service of a "
        "religious group."
    ]

    personality_trait = random.choice(acolyte_personality_trait)
    ideal = random.choice(acolyte_ideal)
    bond = random.choice(acolyte_bond)
    flaw = random.choice(acolyte_flaw)
    origin_xgte = random.choice(acolyte_origin_xgte)

    return personality_trait, ideal, bond, flaw, origin_xgte


def charlatan_background():
    charlatan_scam = [
        "I cheat at games of chance.",
        "I shave coins or forge documents",
        "I insinuate myself into people's lives to prey on their weakness and secure their fortunes.",
        "I put on new identities like clothes.",
        "I run sleight-of-hand cons on street corners.",
        "I convince people that worthless junk is worth their hard-earned money."
    ]

    charlatan_personality_trait = [
        "I fall in and out of love easily, and am always pursuing someone.",
        "I have a joke for every occasion, especially occasions where humour is inappropriate.",
        "Flattery is my preferred trick for getting what I want.",
        "I'm a born gambler who can't resist taking a risk for a potential payoff.",
        "I lie about almost everything, even when there's no good reason to.",
        "Sarcasm and insults are my weapons of choice.",
        "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        "I pocket anything I see that might have any value."
    ]

    charlatan_ideal = [
        "Independence. I am a free spirit - no one tells me what to do. (Chaotic).",
        "Fairness. I never target people who can't afford to lose a few coins. (Lawful).",
        "Charity. I distribute the money I acquire to the people who really need it. (Good).",
        "Creativity. I never run the same con twice. (Chaotic).",
        "Friendship. Material goods come and go. Bonds of friendship last forever. (Good).",
        "Aspiration. I'm determined to make something of myself. (Any)."
    ]

    charlatan_bond = [
        "I fleeced the wrong person and must work to ensure this individual never crosses paths with me or those I "
        "care about",
        "I owe everything to my mentor - a horrible person who's probably rotting in jail somewhere.",
        "Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her.",
        "I come from a noble family, and one day I'll reclaim my lands for and title from those who stole them from "
        "me.",
        "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
        "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able "
        "to forgive myself."
    ]

    charlatan_flaw = [
        "I can't resist a pretty face",
        "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        "I'm convinced that no one could ever fool me in the way I fool others.",
        "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
        "I can't resist swindling people who are more powerful than me.",
        "I hate to admit it and will hate myself for it, bit I'll run and preserve my own hide if the going gets tough."
    ]

    charlatan_origin_xgte = [
        "I was left to my own devices, and my knack for manipulating others helped me survive.",
        "I learned early on that people are gullible and easy to exploit.",
        "I often got in trouble, but I managed to talk my way out of it every time.",
        "I took up with a confidence artist, from whom I learned my craft.",
        "After a charlatan fleeced my family, I decided to learn the trade so I would never be fooled by such "
        "deception again.",
        "I was poor or I feared becoming poor, so I learned the tricks I needed to keep myself out of poverty."
    ]

    scam = random.choice(charlatan_scam)
    personality_trait = random.choice(charlatan_personality_trait)
    ideal = random.choice(charlatan_ideal)
    bond = random.choice(charlatan_bond)
    flaw = random.choice(charlatan_flaw)
    origin_xgte = random.choice(charlatan_origin_xgte)

    return personality_trait, ideal, bond, flaw, scam, origin_xgte


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

    criminal_origin_xgte = [
        "I resented authority in my younger days and saw a life of crime as the best way to fight against tyranny and "
        "oppression.",
        "Necessity forced me to take up the life, since it was the only way I could survive.",
        "I fell in with a gang of reprobates and ne'er-do wells, and I learned my specialty from them.",
        "A parent or relative taught me my criminal specialty to prepare me for the family business.",
        "I left home and found a place in a thieves' guild or some other criminal organization.",
        "I was always bored, so I turned to crime to pass the time and discovered I was quite good at it."
    ]

    specialty = random.choice(criminal_speciality)
    personality_trait = random.choice(criminal_personality_trait)
    ideal = random.choice(criminal_ideal)
    bond = random.choice(criminal_bond)
    flaw = random.choice(criminal_flaw)
    origin_xgte = random.choice(criminal_origin_xgte)

    return personality_trait, ideal, bond, flaw, specialty, origin_xgte


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

    entertainer_origin_xgte = [
        "Members of my family made ends meet by performing, so it was fitting for me to follow their example.",
        "I always had a keen insight into other people, enough so that I could make them laugh or cry with my stories "
        "or songs.",
        "I ran away from home to follow a minstrel troupe.",
        "I saw a bard perform once, and I knew from that moment on what I was born to do.",
        "I earned coin by performing on street corners and eventually made a name for myself.",
        "A traveling entertainer took me in and taught me the trade.",
    ]

    routine = random.choice(entertainer_routines)
    personality_trait = random.choice(entertainer_personality_trait)
    ideal = random.choice(entertainer_ideal)
    bond = random.choice(entertainer_bond)
    flaw = random.choice(entertainer_flaw)
    origin_xgte = random.choice(entertainer_origin_xgte)

    return personality_trait, ideal, bond, flaw, routine, origin_xgte


def folk_hero_background():
    folk_hero_defining_event = [
        "I stood up to a tyrant's agents.",
        "I saved people during a natural disaster.",
        "I stood alone against a terrible monster.",
        "I stole from a corrupt merchant to help the poor.",
        "I led a militia to fight off an invading army.",
        "I broke into a tyrant's castle and stole weapons to arm the people.",
        "I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.",
        "A lord rescinded an unpopular decree after I led a symbolic act of protect against it.",
        "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
        "Recruited into a lord's army, I rose to leadership and was commended for my heroism."
    ]

    folk_hero_personality_trait = [
        "I judge people by their actions, not their words.",
        "If someone is in trouble, I'm always ready to lend help.",
        "When I set my mind to something, I follow through no matter what gets in my way.",
        "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
        "I'm confident in my own abilities and do what I can to instill confidence in others.",
        "Thinking is for other people. I prefer action.",
        "I misuse long words in an attempt to sound smarter.",
        "I get bored easily. When am I going to get on with my destiny?"
    ]

    folk_hero_ideal = [
        "Respect. People deserve to be treated with dignity and respect. (Good)",
        "Fairness. No one should get preferential treatment before the law, and no one is above the law. (Lawful)",
        "Freedom. Tyrants must not be allowed to oppress the people. (Chaotic)",
        "Might. If I become strong, I can take what I want – what I deserve. (Evil)",
        "Sincerity. There's no good in pretending to be something I'm not. (Neutral)",
        "Destiny. Nothing and no one can steer me away from my higher calling. (Any)"
    ]

    folk_hero_bond = [
        "I have a family, but I have no idea where they are. One day, I hope to see them again.",
        "I worked the land, I love the land, and I will protect the land.",
        "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
        "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
        "I protect those who cannot protect themselves.",
        "I wish my childhood sweetheart had come with me to pursue my destiny."
    ]

    folk_hero_flaw = [
        "The tyrant who rules my land will stop at nothing to see me killed.",
        "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
        "The people who knew me when I was young know my shameful secret, so I can never go home again.",
        "I have a weakness for the vices of the city, especially hard drink.",
        "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
        "I have trouble trusting in my allies."
    ]

    folk_hero_origin_xgte = [
        "I learned what was right and wrong from my family.",
        "I was always enamored by tales of heroes and wished I could be something more than ordinary.",
        "I hated my mundane life, so when it was time for someone to step up and do the right thing, I took my chance.",
        "A parent or one of my relatives was an adventurer, and I was inspired by that person's courage.",
        "A mad old hermit spoke a prophecy when I was born, saying that I would accomplish great things.",
        "I have always stood up for those who are weaker than I am."
    ]

    defining_event = random.choice(folk_hero_defining_event)
    personality_trait = random.choice(folk_hero_personality_trait)
    ideal = random.choice(folk_hero_ideal)
    bond = random.choice(folk_hero_bond)
    flaw = random.choice(folk_hero_flaw)
    origin_xgte = random.choice(folk_hero_origin_xgte)

    return personality_trait, ideal, bond, flaw, defining_event, origin_xgte


def guild_artisan_background():
    guild_business = [
        "Alchemists and apothecaries",
        "Armorers, locksmiths, and finesmiths",
        "Brewers, distillers, and vintners",
        "Calligraphers, scribes, and scriveners",
        "Carpenters, roofers, and plasterers",
        "Cartographers, surveyors, and chart-makers",
        "Cobblers and shoemakers",
        "Cooks and bakers",
        "Glassblowers and glaziers",
        "Jewelers and gemcutters",
        "Leatherworkers, skinners, and tanners",
        "Masons and stonecutters",
        "Painters, limners, and sign-makers",
        "Potters and tile-makers",
        "Shipwrights and sailmakers",
        "Smiths and metal-forgers",
        "Tinkers, pewterers, and casters",
        "Wagon-makers and wheelwrights",
        "Weavers and dyers",
        "Woodcarvers, coopers, and bowyers"
    ]

    guild_artisan_personality_traits = [
        "I believe that anything worth doing is worth doing right. I can't help it – I'm a perfectionist.",
        "I'm a snob who looks down on those who can't appreciate fine art.",
        "I always want to know how things work and what makes people tick.",
        "I'm full of witty aphorisms and have a proverb for every occasion.",
        "I'm rude to people who lack my commitment to hard work and fair play.",
        "I like to talk at length about my profession.",
        "I don't part with my money easily and will haggle tirelessly to get the best deal possible.",
        "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when "
        "people haven't heard of me."
    ]

    guild_artisan_ideal = [
        "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of "
        "civilization. (Lawful)",
        "Generosity. My talents were given to me so that I could use them to benefit the world. (Good)",
        "Freedom. Everyone should be free to pursue his or her own livelihood. (Chaotic)",
        "Greed. I'm only in it for the money. (Evil)",
        "People. I'm committed to the people I care about, not to ideals. (Neutral)",
        "Aspiration. I work hard to be the best there is at my craft."
    ]

    guild_artisan_bonds = [
        "The workshop where I learned my trade is the most important place in the world to me.",
        "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for "
        "someone worthy.",
        "I owe my guild a great debt for forging me into the person I am today.",
        "I pursue wealth to secure someone's love.",
        "One day I will return to my guild and prove that I am the greatest artisan of them all.",
        "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
    ]

    guild_artisan_flaws = [
        "I'll do anything to get my hands on something rare or priceless.",
        "I'm quick to assume that someone is trying to cheat me.",
        "No one must ever learn that I once stole money from guild coffers.",
        "I'm never satisfied with what I have – I always want more.",
        "I would kill to acquire a noble title.",
        "I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals."
    ]

    guild_artisan_origin_xgte = [
        "I was apprenticed to a master who taught me the guild's business.",
        "I helped a guild artisan keep a secret or complete a task, and in return I was taken on as an apprentice.",
        "One of my family members who belonged to the guild made a place for me.",
        "I was always good with my hands, so I took the opportunity to learn a trade.",
        "I wanted to get away from my home situation and start a new life.",
        "I learned the essentials of my craft from a mentor but had to join the guild to finish my training."
    ]

    guild_business = random.choice(guild_business)
    personality_trait = random.choice(guild_artisan_personality_traits)
    ideal = random.choice(guild_artisan_ideal)
    bond = random.choice(guild_artisan_bonds)
    flaw = random.choice(guild_artisan_flaws)
    origin_xgte = random.choice(guild_artisan_origin_xgte)

    return personality_trait, ideal, bond, flaw, guild_business, origin_xgte


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

    hermit_origin_xgte = [
        "My enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.",
        "I am comfortable with being isolated, as I seek inner peace.",
        "I never liked the people I called my friends, so it was easy for me to strike out on my own.",
        "I felt compelled to forsake my past, but did so with great reluctance, and sometimes I regret making that "
        "decision.",
        "I lost everything-my home, my family, my friends. Going it alone was all I could do.",
        "Society's decadence disgusted me, so I decided to leave it behind."
    ]

    life_of_seclusion = random.choice(hermit_life_of_seclusion)
    personality_trait = random.choice(hermit_personality_traits)
    ideal = random.choice(hermit_ideals)
    bond = random.choice(hermit_bonds)
    flaw = random.choice(hermit_flaw)
    origin_xgte = random.choice(hermit_origin_xgte)

    return personality_trait, ideal, bond, flaw, life_of_seclusion, origin_xgte


def noble_background():
    noble_personality_trait = [
        "My eloquent flattery makes everyone I talk to feel like the most wonderful and important "
        "person in the world.",
        "The common folk love me for my kindness and generosity.",
        "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
        "I take great pains to always look my best and follow the latest fashions.",
        "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
        "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
        "My favor, once lost, is lost forever.",
        "If you do me an injury, I will crush you, ruin your name, and salt your fields."
    ]

    noble_ideal = [
        "Respect. Respect is due to me because of my position, but all people regardless of station "
        "deserve to be treated with dignity. (Good)",
        "Responsibility. It is my duty to respect the authority of those above me, just as those below "
        "me must respect mine. (Lawful)",
        "Independence. I must prove that I can handle myself without the coddling of my family. "
        "(Chaotic)",
        "Power. If I can attain more power, no one will tell me what to do. (Evil)",
        "Family. Blood runs thicker than water. (Any)",
        "Noble Obligation. It is my duty to protect and care for the people beneath me. (Good)"
    ]

    noble_bond = [
        "I will face any challenge to win the approval of my family.",
        "My house’s alliance with another noble family must be sustained at all costs.",
        "Nothing is more important than the other members of my family.",
        "I am in love with the heir of a family that my family despises.",
        "My loyalty to my sovereign is unwavering.",
        "The common folk must see me as a hero of the people."
    ]

    noble_flaw = [
        "I secretly believe that everyone is beneath me.",
        "I hide a truly scandalous secret that could ruin my family forever.",
        "I too often hear veiled insults and threats in every word addressed to me, and I'm quick to "
        "anger.",
        "I have an insatiable desire for carnal pleasures.",
        "In fact, the world does revolve around me.",
        "By my words and actions, I often bring shame to my family."
    ]

    noble_origin_xgte = [
        "I come from an old and storied family, and it fell to me to preserve the family name.",
        "My family has been disgraced, and I intend to clear our name.",
        "My family recently came by its title, and that elevation thrust us into a new and strange world.",
        "My family has a title, but none of my ancestors have distinguished themselves since we gained it.",
        "My family is filled with remarkable people. I hope to live up to their example.",
        "I hope to increase my family's power and influence."
    ]

    personality_trait = random.choice(noble_personality_trait)
    ideal = random.choice(noble_ideal)
    bond = random.choice(noble_bond)
    flaw = random.choice(noble_flaw)
    origin_xgte = random.choice(noble_origin_xgte)

    return personality_trait, ideal, bond, flaw, origin_xgte


def outlander_background():
    outlander_origin = [
        "Forester",
        "Trapper",
        "Homesteader",
        "Guide",
        "Exile or outcast",
        "Bounty hunter",
        "Pilgrim",
        "Tribal nomad",
        "Hunter-gatherer",
        "Tribal marauder"
    ]

    outlander_personality_trait = [
        "I'm driven by a wanderlust that led me away from home.",
        "I watch over my friends as if they were a litter of newborn pups.",
        "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde. "
        "I'd do it again if I had to.",
        "I have a lesson for every situation, drawn from observing nature.",
        "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a "
        "hungry owlbear.",
        "I'm always picking things up, absently fiddling with them, and sometimes accidentally "
        "breaking them.",
        "I feel far more comfortable around animals than people.",
        "I was, in fact, raised by wolves."
    ]

    outlander_ideals = [
        "Change. Life is like the seasons, in constant change, and we must change with it. (Chaotic)",
        "Greater Good. It is each person's responsibility to make the most happiness for the whole "
        "tribe. (Good)",
        "Honor. If I dishonor myself, I dishonor my whole clan. (Lawful)",
        "Might. The strongest are meant to rule. (Evil)",
        "Nature. The natural world is more important than all the constructs of civilization. "
        "(Neutral)",
        "Glory. I must earn glory in battle, for myself and my clan. (Any)"
    ]

    outlander_bonds = [
        "My family, clan, or tribe is the most important thing in my life, even when they are far "
        "from me.",
        "An injury to the unspoiled wilderness of my home is an injury to me.",
        "I will bring terrible wrath down on the evildoers who destroyed my homeland.",
        "I am the last of my tribe, and it is up to me to ensure their names enter legend.",
        "I suffer awful visions of a coming disaster and will do anything to prevent it.",
        "It is my duty to provide children to sustain my tribe."
    ]

    outlander_flaws = [
        "I am too enamored of ale, wine, and other intoxicants.",
        "There's no room for caution in a life lived to the fullest.",
        "I remember every insult I've received and nurse a silent resentment toward anyone who's ever "
        "wronged me.",
        "I am slow to trust members of other races, tribes, and societies.",
        "Violence is my answer to almost any challenge.",
        "Don't expect me to save those who can't save themselves. It is nature's way that the strong "
        "thrive and the weak perish.",
    ]

    outlander_origin_xtge = [
        "I spent a lot of time in the wilderness as a youngster, and I came to love that way of life.",
        "From a young age, I couldn't abide the stink of the cities and preferred to spend my time in nature.",
        "I came to understand the darkness that lurks in the wilds, and I vowed to combat it.",
        "My people lived on the edges of civilization, and I learned the methods of survival from my family.",
        "After a tragedy I retreated to the wilderness, leaving my old life behind.",
        "My family moved away from civilization, and I learned to adapt to my new environment."
    ]

    origin = random.choice(outlander_origin)
    personality_trait = random.choice(outlander_personality_trait)
    ideal = random.choice(outlander_ideals)
    bond = random.choice(outlander_bonds)
    flaw = random.choice(outlander_flaws)
    origin_xgte = random.choice(outlander_origin_xtge)

    return personality_trait, ideal, bond, flaw, origin, origin_xgte


def sage_background():
    sage_speciality = [
        "Alchemist",
        "Astronomer",
        "Discredited academic",
        "Librarian",
        "Professor",
        "Researcher",
        "Wizard's apprentice",
        "Scribe"
    ]

    sage_personality_trait = [
        "I use polysyllabic words that convey the impression of great erudition.",
        "I've read every book in the world's greatest libraries - or I like to boast that I have.",
        "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything "
        "and everything to others.",
        "There's nothing I like more than a good mystery.",
        "I'm willing to listen to every side of an argument before I make my own judgment.",
        "I... speak... slowly... when talking... to idiots,... which... almost... everyone... is... compared... to me.",
        "I am horribly, horribly awkward in social situations.",
        "I'm convinced that people are always trying to steal my secrets."
    ]

    sage_ideal = [
        "Knowledge. The path to power and self-improvement is through knowledge. (Neutral)",
        "Beauty. What is beautiful points us beyond itself toward what is true. (Good)",
        "Logic. Emotions must not cloud our logical thinking. (Lawful)",
        "No Limits. Nothing should fetter the infinite possibility inherent in all existence. "
        "(Chaotic)",
        "Power. Knowledge is the path to power and domination. (Evil)",
        "Self-Improvement. The goal of a life of study is the betterment of oneself. (Any)"
    ]

    sage_bonds = [
        "It is my duty to protect my students.",
        "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
        "I work to preserve a library, university, scriptorium, or monastery.",
        "My life's work is a series of tomes related to a specific field of lore.",
        "I've been searching my whole life for the answer to a certain question.",
        "I sold my soul for knowledge. I hope to do great deeds and win it back."
    ]

    sage_flaws = [
        "I am easily distracted by the promise of information.",
        "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
        "Unlocking an ancient mystery is worth the price of a civilization.",
        "I overlook obvious solutions in favor of complicated ones.",
        "I speak without really thinking through my words, invariably insulting others.",
        "I can't keep a secret to save my life, or anyone else's."
    ]

    sage_origin_xgte = [
        "I was naturally curious, so I packed up and went to a university to learn more about the world.",
        "My mentor's teachings opened my mind to new possibilities in that field of study.",
        "I was always an avid reader, and I learned much about my favorite topic on my own.",
        "I discovered an old library and pored over the texts I found there. That experience awakened a hunger for "
        "more knowledge.",
        "I impressed a wizard who told me I was squandering my talents and should seek out an education to take "
        "advantage of my gifts.",
        "One of my parents or a relative gave me a basic education that whetted my appetite, and I left home to build "
        "on what I had learned."
    ]

    speciality = random.choice(sage_speciality)
    personality_trait = random.choice(sage_personality_trait)
    ideal = random.choice(sage_ideal)
    bond = random.choice(sage_bonds)
    flaw = random.choice(sage_flaws)
    origin_xgte = random.choice(sage_origin_xgte)

    return personality_trait, ideal, bond, flaw, speciality, origin_xgte


def sailor_background():
    sailor_personality_trait = [
        "My friends know they can rely on me, no matter what.",
        "I work hard so that I can play hard when the work is done.",
        "I enjoy sailing into new ports and making new friends over a flagon of ale.",
        "I stretch the truth for the sake of a good story.",
        "To me, a tavern brawl is a nice way to get to know a new city.",
        "I never pass up a friendly wager.",
        "My language is as foul as an otyugh nest.",
        "I like a job well done, especially if I can convince someone else to do it."
    ]

    sailor_ideals = [
        "Respect. The thing that keeps a ship together is mutual respect between captain and crew. "
        "(Good)",
        "Fairness. We all do the work, so we all share in the rewards. (Lawful)",
        "Freedom. The sea is freedom-the freedom to go anywhere and do anything. (Chaotic)",
        "Mastery. I'm a predator, and the other ships on the sea are my prey. (Evil)",
        "People. I'm committed to my crewmates, not to ideals. (Neutral)",
        "Aspiration. Someday I'll own my own ship and chart my own destiny. (Any)",
    ]

    sailor_bonds = [
        "I'm loyal to my captain first, everything else second.",
        "The ship is most important - crewmates and captains come and go.",
        "I'll always remember my first ship.",
        "In a harbor town, I have a paramour whose eyes nearly stole me from the sea.",
        "I was cheated out of my fair share of the profits, and I want to get my due.",
        "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. "
        "Vengeance will be mine."
    ]

    sailor_flaws = [
        "I follow orders, even if I think they're wrong.",
        "I'll say anything to avoid having to do extra work.",
        "Once someone questions my courage, I never back down no matter how dangerous the situation.",
        "Once I start drinking, it's hard for me to stop.",
        "I can't help but pocket loose coins and other trinkets I come across.",
        "My pride will probably lead to my destruction."
    ]

    sailor_origin_xgte = [
        "I was press-ganged by pirates and forced to serve on their ship until I finally escaped.",
        "I wanted to see the world, so I signed on as a deckhand for a merchant ship.",
        "One of my relatives was a sailor who took me to sea.",
        "I needed to escape my community quickly, so I stowed away on a ship. When the crew found me, I was forced "
        "to work for my passage.",
        "Reavers attacked my community, so I found refuge on a ship until I could seek vengeance.",
        "I had few prospects where I was living, so I left to find my fortune elsewhere."
    ]

    personality_trait = random.choice(sailor_personality_trait)
    ideal = random.choice(sailor_ideals)
    bond = random.choice(sailor_bonds)
    flaw = random.choice(sailor_flaws)
    origin_xgte = random.choice(sailor_origin_xgte)

    return personality_trait, ideal, bond, flaw, origin_xgte


def soldier_background():
    soldier_speciality = [
        "Officer",
        "Scout",
        "Infantry",
        "Cavalry",
        "Healer",
        "Quartermaster",
        "Standard bearer",
        "Support staff (cook, blacksmith, or the like)"
    ]

    soldier_personality_traits = [
        "I'm always polite and respectful.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost "
        "every combat situation.",
        "I can stare down a hell hound without flinching.",
        "I enjoy being strong and like breaking things.",
        "I have a crude sense of humor.",
        "I face problems head-on. A simple, direct solution is the best path to success."
    ]

    soldier_ideals = [
        "Greater Good. Our lot is to lay down our lives in defense of others. (Good)",
        "Responsibility. I do what I must and obey just authority. (Lawful)",
        "Independence. When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)",
        "Might. In life as in war, the stronger force wins. (Evil)",
        "Live and Let Live. Ideals aren't worth killing over or going to war for. (Neutral)",
        "Nation. My city, nation, or people are all that matter. (Any)"
    ]

    soldier_bonds = [
        "I would still lay down my life for the people I served with.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "My honor is my life.",
        "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
        "Those who fight beside me are those worth dying for.",
        "I fight for those who cannot fight for themselves."
    ]

    soldier_flaws = [
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I have little respect for anyone who is not a proven warrior.",
        "I made a terrible mistake in battle that cost many lives - and I would do anything to keep "
        "that mistake secret.",
        "My hatred of my enemies is blind and unreasoning.",
        "I obey the law, even if the law causes misery.",
        "I'd rather eat my armor than admit when I'm wrong.",
    ]

    soldier_origin_xgte = [
        "I joined the militia to help protect my community from monsters.",
        "A relative of mine was a soldier, and I wanted to carry on the family tradition .",
        "The local lord forced me to enlist in the army.",
        "War ravaged my homeland while I was growing up. Fighting was the only life I ever knew.",
        "I wanted fame and fortune, so I joined a mercenary company, selling my sword to the highest bidder.",
        "Invaders attacked my homeland. It was my duty to take up arms in defense of my people."
    ]

    soldier_speciality = random.choice(soldier_speciality)
    personality_trait = random.choice(soldier_personality_traits)
    ideal = random.choice(soldier_ideals)
    bond = random.choice(soldier_bonds)
    flaw = random.choice(soldier_flaws)
    origin_xgte = random.choice(soldier_origin_xgte)

    return personality_trait, ideal, bond, flaw, soldier_speciality, origin_xgte


def urchin_background():
    urchin_personality_trait = [
        "I hide scraps of food and trinkets away in my pockets.",
        "I ask a lot of questions.",
        "I like to squeeze into small places where no one else can get to me.",
        "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
        "I eat like a pig and have bad manners.",
        "I think anyone who's nice to me is hiding evil intent.",
        "I don't like to bathe.",
        "I bluntly say what other people are hinting at or hiding."
    ]

    urchin_ideals = [
        "Respect. All people, rich or poor, deserve respect. (Good)",
        "Community. We have to take care of each other, because no one else is going to do it. "
        "(Lawful)",
        "Change. The low are lifted up, and the high and mighty are brought down. Change is the "
        "nature of things. (Chaotic)",
        "Retribution. The rich need to be shown what life and death are like in the gutters. (Evil)",
        "People. I help the people who help me-that's what keeps us alive. (Neutral)",
        "Aspiration. I'm going to prove that I'm worthy of a better life. (Any)"
    ]

    urchin_bonds = [
        "My town or city is my home, and I'll fight to defend it.",
        "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
        "I owe my survival to another urchin who taught me to live on the streets.",
        "I owe a debt I can never repay to the person who took pity on me.",
        "I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
        "No one else should have to endure the hardships I've been through."
    ]

    urchin_flaws = [
        "If I'm outnumbered, I will run away from a fight.",
        "Gold seems like a lot of money to me, and I'll do just about anything for more of it.",
        "I will never fully trust anyone other than myself.",
        "I'd rather kill someone in their sleep then fight fair.",
        "It's not stealing if I need it more than someone else.",
        "People who can't take care of themselves get what they deserve."
    ]

    urchin_origin_xgte = [
        "Wanderlust caused me to leave my family to see the world. I look after myself.",
        "I ran away from a bad situation at home and made my own way in the world.",
        "Monsters wiped out my village, and I was the sole survivor. I had to find a way to survive.",
        "A notorious thief looked after me and other orphans, and we spied and stole to earn our keep.",
        "One day I woke up on the streets, alone and hungry, with no memory of my early childhood.",
        "My parents died, leaving no one to look after me. I raised myself."
    ]

    personality_trait = random.choice(urchin_personality_trait)
    ideal = random.choice(urchin_ideals)
    bond = random.choice(urchin_bonds)
    flaw = random.choice(urchin_flaws)
    origin_xgte = random.choice(urchin_origin_xgte)

    return personality_trait, ideal, bond, flaw, origin_xgte
