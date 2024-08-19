"""Calculates the least amount of levels needed to create a Rainbow Warrior in D&D 5e as of 08/15/2024"""
"""All lists will have a Level 1 Genie Warlock as it is the only way to get Bludgeoning"""
"""Poison is implied via imbuing your weapon, Slashing is implied via using a slashing weapon"""

from pprint import pprint

from damage_type import Damage_Type
# from dnd_class import Dnd_Class

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
    "Background": {"Strike of the Giants": (Damage_Type.LIGHTNING)},
    "Cantrip": {"Booming Blade": (Damage_Type.THUNDER)},
    "Classes": {
        "Warlock": ("Genie", (Damage_Type.BLUDGEONING), 1),
        "Blood Hunter": ("", (Damage_Type.COLD), 2),
        "Bard": ("Whispers", (Damage_Type.PSYCHIC), 4), # Listed as 4 as will be increased by 1 from feat
        "Ranger": ("Swarmkeeper", (Damage_Type.PIERCING), 4), # Listed as 4 as will be increased by 1 from feat
        "Fighter": ("Rune", (Damage_Type.FIRE), 3),
    },
    "Concentration": {"Zephyr Strike": (Damage_Type.FORCE)},
    "Feats": {
        "Vital Sacrifice": (Damage_Type.NECROTIC),
        "Gift of the Chromatic Dragon: Acid": (Damage_Type.ACID),
    },
    "Species": {"Aasimar: Radiant": (Damage_Type.RADIANT)},
    "Level": 14,
}

mockup_sources_missing_fields = {
    "Background": {},
    "Cantrip": {"Booming Blade": (Damage_Type.THUNDER)},
    "Classes": {
        "Warlock": ("Genie", (Damage_Type.BLUDGEONING), 1),
        "Bard": ("Whispers", (Damage_Type.PSYCHIC), 4), # Listed as 4 as will be increased by 1 from feat
        "Ranger": ("Swarmkeeper", (Damage_Type.PIERCING), 4), # Listed as 4 as will be increased by 1 from feat
        "Fighter": ("Rune", (Damage_Type.FIRE), 3),
    },
    "Concentration": {},
    "Feats": {
        "Vital Sacrifice": (Damage_Type.NECROTIC),
        "Gift of the Chromatic Dragon: Acid": (Damage_Type.ACID),
    },
    "Species": {},
    "Level": 14,
}

mockup_sources_no_filled_fields = {
    "Background": {},
    "Cantrip": {},
    "Classes": {},
    "Concentration": {},
    "Feats": {},
    "Species": {},
    "Level": 14,
}

mockup_master_list = {
    0: mockup_sources,
    1: mockup_sources_missing_fields,
    2: mockup_sources_no_filled_fields,
}

mockup_classes_dict = {
    "Warlock": ("Genie", (Damage_Type.BLUDGEONING), 1),
    "Blood Hunter": ("", (Damage_Type.COLD), 2),
    "Bard": ("Whispers", (Damage_Type.PSYCHIC), 4),
    "Ranger": ("Swarmkeeper", (Damage_Type.PIERCING), 4),
    "Fighter": ("Rune", (Damage_Type.FIRE), 3),
}


def add_class_levels(class_dict: dict) -> int:
    """Adds levels from a given dict of early draft classes"""
    levels = 0
    for attributes in class_dict.values():
        levels += attributes[2]
    return levels


def check_if_source_is_empty(dictionary: dict, source_name: str) -> bool:
    return dictionary[source_name] == {}


def check_which_sources_are_empty(dictionary: dict) -> dict:
    sources_empty = {}
    for source_name in dictionary.keys():
        if source_name != "Level":
            sources_empty[source_name] = check_if_source_is_empty(dictionary,source_name)
    return sources_empty


def check_which_dicts_are_empty(master_source_list: dict[dict]) -> dict[dict]:
    master_source_list_empties = {}
    for source_list_name in master_source_list.keys():
        master_source_list_empties[source_list_name] = check_which_sources_are_empty(master_source_list[source_list_name])
    return master_source_list_empties

def run():
    print_source_list = False
    print_damage_types_list = False
    print_damage_types_enum = False
    pprint_mockup_sources_one_dict = False
    add_class_levels_from_mockup_dict = False
    check_empty_one_source_from_mockup_dict = False
    check_empty_all_sources_from_mockup_dict = False
    check_empty_all_dicts_in_master_dict = True

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
    if print_damage_types_enum:
        print("Damage Types via enum: ")
        for damage in Damage_Type:
            print("\t" + str(damage.name) + ": " + str(damage.value))
            print("")

    # Printing Mockup source dict via pprint
    if pprint_mockup_sources_one_dict:
        pprint(mockup_sources)

    # Printing class level total from mockup dict
    if add_class_levels_from_mockup_dict:
        levels = add_class_levels(mockup_classes_dict)
        print(levels)

    # Printing if a source is empty from mockup dict
    if check_empty_one_source_from_mockup_dict:
        source_empty = check_if_source_is_empty(mockup_sources,"Cantrip")
        print(f"This should be False: {source_empty}")

    # Printing if source list is empty form mockup dict
    if check_empty_all_sources_from_mockup_dict:
        sources_empty = check_which_sources_are_empty(mockup_sources)
        pprint(sources_empty)

    # Printing if master source list is empty from mockup master list
    if check_empty_all_dicts_in_master_dict:
        masters_empty = check_which_dicts_are_empty(mockup_master_list)
        pprint(masters_empty)

run()