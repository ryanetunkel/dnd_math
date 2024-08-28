"""Calculates the least amount of levels needed to create a Rainbow Warrior in D&D 5e as of 08/15/2024"""
"""All lists will have a Level 1 Genie Warlock as it is the only way to get Bludgeoning"""
"""Poison is implied via imbuing your weapon, Slashing is implied via using a slashing weapon"""

from typing import Optional

from pprint import pprint

from damage_type import Damage_Type
from official_sources import *
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
        "Warlock": {"Genie", (Damage_Type.BLUDGEONING), 1},
        "Blood Hunter": {"None", (Damage_Type.COLD), 2},
        "Bard": {"Whispers", (Damage_Type.PSYCHIC), 4},  # Listed as 4 as will be increased by 1 from feat
        "Ranger": {"Swarmkeeper", (Damage_Type.PIERCING), 4},  # Listed as 4 as will be increased by 1 from feat
        "Fighter": {"Rune", (Damage_Type.FIRE), 3},
    },
    "Concentration": {"Zephyr Strike": (Damage_Type.FORCE)},
    "Feats": {
        "Vital Sacrifice": (Damage_Type.NECROTIC),
        "Gift of the Chromatic Dragon": (Damage_Type.ACID),
    },
    "Species": {"Aasimar": (Damage_Type.RADIANT)},
    "Level": 14,
}

mockup_sources_missing_fields = {
    "Background": {},
    "Cantrip": {"Booming Blade": (Damage_Type.THUNDER)},
    "Classes": {
        "Warlock": {"Genie": ((Damage_Type.BLUDGEONING), 1)},
        "Bard": {"Whispers": ((Damage_Type.PSYCHIC), 4)},  # Listed as 4 as will be increased by 1 from feat
        "Ranger": {"Swarmkeeper": ((Damage_Type.PIERCING), 4)},  # Listed as 4 as will be increased by 1 from feat
        "Fighter": {"Rune": ((Damage_Type.FIRE), 3)},
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

mockup_sources_no_filled_fields_editable = {
    "Background": {},
    "Cantrip": {},
    "Classes": {},
    "Concentration": {},
    "Feats": {},
    "Species": {},
    "Level": 14,
}

mockup_master_dict = {
    0: mockup_sources,
    1: mockup_sources_missing_fields,
    2: mockup_sources_no_filled_fields,
}

mockup_classes_dict = {
    "Warlock": {"Genie": ((Damage_Type.BLUDGEONING), 1),},
    "Blood Hunter": {
        "None_2": ((Damage_Type.COLD), 2),
        "None_6": ((Damage_Type.PSYCHIC), 6),
        "Ghostslayer": ((Damage_Type.RADIANT), 3),
    },
    "Bard": {"Whispers": ((Damage_Type.PSYCHIC), 4),},
    "Ranger": {"Swarmkeeper": ((Damage_Type.PIERCING), 4),},
    "Fighter": {"Rune": ((Damage_Type.FIRE), 3),},
}


def add_class_levels(class_dict: dict[str,dict[str,tuple]]) -> int:
    """Adds levels from a given dict of early draft classes"""
    levels = 0
    for class_name, subclass in class_dict.items():
        subclass_names = subclass.keys()
        levels_to_add = 0
        for subclass_name, attributes in class_dict[class_name].items():
            if len(subclass_names) < 2:  # Accounts for stacking features that give damages without needing a subclass
                levels += attributes[-1]
            elif subclass[subclass_name][-1] > levels_to_add:
                levels_to_add = subclass[subclass_name][-1]
        levels += levels_to_add
    return levels


def check_if_source_is_empty(dictionary: dict, source_name: str) -> bool:
    """Checks if a given source_name in a given dictionary is empty"""
    return dictionary[source_name] == {}


def check_which_sources_are_empty(dictionary: dict) -> dict:
    """Returns a dictionary detailing which source_names within a given dictionary that are empty"""
    sources_empty = {}
    for source_name in dictionary.keys():
        if source_name != "Level":
            sources_empty[source_name] = check_if_source_is_empty(dictionary,source_name)
    return sources_empty


def check_which_dicts_are_empty(master_source_dict: dict[dict]) -> dict[dict]:
    """Returns a dict of dicts detailing which dicts within a given master_source_dict that are empty"""
    master_source_list_empties = {}
    for source_list_name in master_source_dict.keys():
        master_source_list_empties[source_list_name] = check_which_sources_are_empty(master_source_dict[source_list_name])
    return master_source_list_empties


def get_damage_options(source_type_name: str, source_name: str, subclass_name_if_class: Optional[str] = None) -> tuple:  # Doesn't check if already have that type or class or anything else, need to give subclass if is a class
    if source_type_name in official_sources_with_damage_options.keys() and source_name in official_sources_with_damage_options.get(source_type_name).keys():
        master_source_dict = official_sources_with_damage_options
    else:
        master_source_dict = official_all_sources

    damages = master_source_dict.get(source_type_name).get(source_name)
    if source_type_name != "Classes":
        return damages
    else:
        if subclass_name_if_class in damages:
            return damages.get(subclass_name_if_class)[0]
        else:
            return ()


def pick_source_option(
    current_source_dict: dict,
    source_type_name: str,
    available_sources: dict,
    available_source_name: str,
    damage_type: Damage_Type,
    subclass_name: Optional[str] = None,
) -> bool:
    # Don't need to check if available_sources have available source two tiers of dicts deep for feats and classes, already accounted for
    # Need to make sure reqs other than emptiness are accounted for outside of this function
    # Non classes/feats format:
    # source_type_name = {
    #     available_source_name: ()  # Concentrations have class reqs, means their tuple is actually like this: ((),{})
    # } # Feats can have multiple available_source_name: () 's
    # Classes format:
    # source_type_name = {
    #     available_source_name: {
    #         subclass_name: ((Damage_Type,Damage_Type,),int),
    #         subclass_name: ((Damage_Type,Damage_Type,),int),
    #     },
    #     available_source_name: {
    #         subclass_name: ((Damage_Type,),int),
    #     },
    # }

    available_source_subdicts = available_sources.get(source_type_name)
    available_source_attributes = available_source_subdicts.get(available_source_name)
    current_source_subdicts = current_source_dict.get(source_type_name)

    damage_options = get_damage_options(source_type_name,available_source_name,subclass_name)
    valid_damage_option = damage_type in damage_options
    multiple_damage_options = (len(damage_options) >= 2)

    empty_slot = not current_source_dict.get(source_type_name) or not current_source_subdicts.get(available_source_name)

    if success:=(empty_slot or (not current_source_subdicts.get(available_source_name).get(subclass_name))):
        # if source_type_name != "Classes":
        #     current_source_dict.get(source_type_name).update({available_source_name: available_source_attributes})
        # else:
        #     current_source_dict.get(source_type_name).update({available_source_name: {subclass_name: available_source_attributes}})
        current_source_dict.get(source_type_name).update({available_source_name: available_source_attributes})
        if source_type_name == "Classes":
            current_source_dict.get(source_type_name).get(available_source_name).update({subclass_name: available_source_attributes})


        if valid_damage_option and multiple_damage_options:
            if source_type_name not in ["Concentration","Classes"]:
                current_source_dict.get(source_type_name).update({available_source_name: (damage_type)}) # *******I think the bug is here?******* the bug is that blood hunter is getting everything from official source options instead of just the chosen subclass and damage type
            elif source_type_name == "Concentration":
                current_source_dict.get(source_type_name).get(available_source_name)[0] = (damage_type)
            elif source_type_name == "Classes": # Multiple subclasses for one class that can be taken together (non-subclass specific features)
                current_source_dict.get(source_type_name).get(available_source_name).get(subclass_name)[0] = (damage_type)

    return success


def run():
    print_source_list = False
    print_damage_types_list = False
    print_damage_types_enum = False
    pprint_mockup_sources_one_dict = False
    add_class_levels_from_mockup_dict = False
    check_empty_one_source_from_mockup_dict = False
    check_empty_all_sources_from_mockup_dict = False
    check_empty_all_dicts_in_master_dict = False
    pick_single_source_damage_options = False
    pick_single_source_option_mockup_dict = True

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
        print("Mockup sources via dict: ")
        pprint(mockup_sources)
        print("")

    # Printing class level total from mockup dict
    if add_class_levels_from_mockup_dict:
        print("Class level total via mockup classes dict: ")
        levels = add_class_levels(mockup_classes_dict)
        print(levels)
        print("")

    # Printing if a source is empty from mockup dict
    if check_empty_one_source_from_mockup_dict:
        print("Checking if a source is empty via mockup sources: ")
        source_empty = check_if_source_is_empty(mockup_sources,"Cantrip")
        print(f"This should be False: {source_empty}")
        print("")

    # Printing if source list is empty form mockup dict
    if check_empty_all_sources_from_mockup_dict:
        print("Checking which sources are empty in mockup sources")
        sources_empty = check_which_sources_are_empty(mockup_sources)
        pprint(sources_empty)
        print("")

    # Printing if master source list is empty from mockup master list
    if check_empty_all_dicts_in_master_dict:
        print("Checking which dicts are empty in a mockup master dict: ")
        masters_empty = check_which_dicts_are_empty(mockup_master_dict)
        pprint(masters_empty)
        print("")

    # Printing the damage options of a source
    if pick_single_source_damage_options:
        print("Printing damage options of different sources: ")
        pprint(get_damage_options(source_type_name="Classes",source_name="Blood Hunter",subclass_name_if_class="None_2"))
        pprint(get_damage_options(source_type_name="Classes",source_name="Artificer",subclass_name_if_class="Battle Smith"))
        pprint(get_damage_options(source_type_name="Classes",source_name="Cleric",subclass_name_if_class="Nature"))
        pprint(get_damage_options(source_type_name="Background",source_name="Strike of the Giants"))
        pprint(get_damage_options(source_type_name="Feats",source_name=""))
        pprint(get_damage_options(source_type_name="Feats",source_name="Gift of the Chromatic Dragon"))
        pprint(get_damage_options(source_type_name="Feats",source_name="Vital Sacrifice"))
        print("")

    # Printing if a single source is successfully picked from mockup dict
    if pick_single_source_option_mockup_dict:
        # Helpful dictionary refresher
        # dictionary = {}
        # dictionary.update({"Now": "it works"})
        # dictionary.update({"This": "works too?"})
        # dictionary.update({"Now": "this overwrites"})
        mockup_sources_no_filled_fields_editable = {
            "Background": {},
            "Cantrip": {},
            "Classes": {},
            "Concentration": {},
            "Feats": {},
            "Species": {},
            "Level": 14,
        }
        successful = pick_source_option(
            current_source_dict=mockup_sources_no_filled_fields_editable,
            source_type_name="Classes",
            available_sources=official_all_sources,
            available_source_name="Blood Hunter",
            damage_type=Damage_Type.COLD,
            subclass_name="None_2",
        )
        pprint(f"Successful?: {successful}")
        pprint(f"Editable post function: {mockup_sources_no_filled_fields_editable}")
        mockup_sources_no_filled_fields_editable = {}
        mockup_sources_no_filled_fields_editable = mockup_sources_no_filled_fields
        pprint(f"Editable post cleanup: {mockup_sources_no_filled_fields_editable}")


run()