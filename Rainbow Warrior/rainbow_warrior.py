"""Calculates the least amount of levels needed to create a Rainbow Warrior in D&D 5e as of 08/15/2024"""
"""All lists will have a Level 1 Genie Warlock as it is the only way to get Bludgeoning"""
"""Poison is implied via imbuing your weapon, Slashing is implied via using a slashing weapon"""

from pprint import pprint

from damage import Damage


source_types = [
    "Background",
    "Cantrip",
    "Class",
    "Concentration",
    "Feat",
    "Species",
]

damage_types = [
    "Acid",
    "Bludgeoning",
    "Cold",
    "Fire",
    "Force",
    "Lightning",
    "Necrotic",
    "Piercing",
    "Psychic",
    "Radiant",
    "Thunder",
]

mockup_sources = {
    "Background": {"Strike of the Giants": Damage.LIGHTNING},
    "Cantrip": ["Booming Blade", Damage.THUNDER],
    "Classes": {
        "Warlock": ["Genie", 1, [Damage.BLUDGEONING]],
        "Blood Hunter": ["", 2, [Damage.COLD]],
        "Bard": ["Whispers", 4, [Damage.PSYCHIC]], # Listed as 4 as will be increased by 1 from feat
        "Ranger": ["Swarmkeeper", 4, [Damage.PIERCING]], # Listed as 4 as will be increased by 1 from feat
        "Fighter": ["Rune", 3, [Damage.FIRE]],
    },
    "Concentration": ["Zephyr Strike", Damage.FORCE],
    "Feats": [["Vital Sacrifice", Damage.NECROTIC], ["Gift of the Chromatic Dragon: Acid", Damage.ACID]],
    "Species": ["Aasimar: Radiant", Damage.RADIANT],
    "Level": 14,
}


def run():
    print_source_list = False
    print_damage_types_list = False
    print_damage_types_enum = False
    pprint_mockup_sources_one_dict = True

    # Printing 1st Draft Source List
    if print_source_list:
        print("Sources: ")
        for source in source_types:
            print("\t" + source)
        print("")

    # Printing 1st Draft Damage Types from list
    if print_damage_types_list:
        print("Damage Types via list: ")
        for damage in damage_types:
            print("\t" + damage)
        print("")

    # Printing 2nd Draft Damage Types via enum
    print("Damage Types via list: ")
    if print_damage_types_enum:
        for damage in Damage:
            print("\t" + str(damage.name) + ": " + str(damage.value))
            print("")

    if pprint_mockup_sources_one_dict:
        pprint(mockup_sources)

run()