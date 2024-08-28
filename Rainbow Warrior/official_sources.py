"""Contains the all_sources dictionary containing all possible source options"""

from damage_type import Damage_Type

official_all_sources = {
    "Background": {
        "Strike of the Giants": (
            Damage_Type.COLD,
            Damage_Type.FIRE,
            Damage_Type.FORCE,
            Damage_Type.LIGHTNING,
            Damage_Type.THUNDER,
        ),
    },
    "Cantrip": {
        "Booming Blade": (Damage_Type.THUNDER),
        "Green-Flame Blade": (Damage_Type.FIRE),
    },
    "Classes": {
        "None": {
            "None": ((), 0),
        },
        "Artificer": {
            "Battle Smith": ((Damage_Type.FORCE), 9),
        },
        "Bard": {
            "Creation": ((Damage_Type.THUNDER), 3),
            "Whispers": ((Damage_Type.PSYCHIC), 3),
        },
        "Blood Hunter": {
            "None_2": ((
                Damage_Type.COLD,
                Damage_Type.FIRE,
                Damage_Type.LIGHTNING
            ), 2),
            "None_6": ((Damage_Type.PSYCHIC), 6),
            "Ghostslayer": ((Damage_Type.RADIANT), 3),
        },
        "Cleric": {
            "Death": ((Damage_Type.NECROTIC), 2),
            "Forge": ((Damage_Type.FIRE), 8),
            "Life": ((Damage_Type.RADIANT), 8),
            "Nature": ((
                Damage_Type.COLD,
                Damage_Type.FIRE,
                Damage_Type.LIGHTNING
            ), 8),
            "Order": ((Damage_Type.PSYCHIC), 8),
            "Tempest": ((Damage_Type.THUNDER), 8),
            "Twilight": ((Damage_Type.RADIANT), 8),
        },
        "Druid": {
            "Spores": ((Damage_Type.NECROTIC), 2),
        },
        "Fighter": {
            "Psionic": ((Damage_Type.FORCE), 3),
            "Rune": ((Damage_Type.FIRE), 3),
        },
        "Paladin": {
            "None_2": ((Damage_Type.RADIANT), 2),
        },
        "Ranger": {
            "Swarmkeeper": ((Damage_Type.PIERCING), 3),
        },
        "Warlock": {
            "None_5": ((Damage_Type.FORCE), 5),
            "Genie": ((Damage_Type.BLUDGEONING), 1),
        },
    },
    "Concentration": {
        # First Level Spells
        "Ensnaring Strike": (
            (Damage_Type.PIERCING), {
                "Paladin": ("Ancients", 3),
                "Ranger": ("None", 2),
            },
        ),
        "Searing Smite": (
            (Damage_Type.FIRE), {
                "Cleric": ("Forge", 1),
                "Paladin": ("None", 2),
            },
        ),
        "Thunderous Smite": (
            (Damage_Type.THUNDER), {
                "Paladin": ("None", 2),
            },
        ),
        "Wrathful Smite": (
            (Damage_Type.FIRE), {
                "Cleric": ("Forge", 1),
                "Paladin": ("None", 2),
            },
        ),
        "Zephyr Strike": (
            ((Damage_Type.FORCE), {
                "Ranger": ("None", 2),
            }),
        ),
        # Second Level Spells
        "Branding Smite": (
            (Damage_Type.RADIANT), {
                "Artificer": ("Battle Smith", 5),
            },
        ),
        # Third Level Spells
        "Elemental Weapon": (
            (
                Damage_Type.ACID,
                Damage_Type.COLD,
                Damage_Type.FIRE,
                Damage_Type.LIGHTNING,
                Damage_Type.THUNDER
            ), {
                "Artificer": ("None", 9),
                "Cleric": ("Forge", 5),
                "Paladin": ("None", 9),
            },
        ),
        "Spirit Shroud": (
            (
                Damage_Type.COLD,
                Damage_Type.NECROTIC,
                Damage_Type.RADIANT,
            ), {
                "Cleric": ("None", 5),
                "Paladin": ("None", 9),
                "Warlock": ("None", 5),
                "Wizard": ("None", 5),
            },
        ),
        "Crusader's Mantle": (
            (Damage_Type.RADIANT), {
                "Cleric": ("War", 5),
            },
        ),
        "Bestow Curse": (
            (Damage_Type.NECROTIC), {
                "Bard": ("None", 5),
                "Cleric": ("None", 5),
                "Paladin": ((
                    "Conquest",
                    "Oathbreaker",
                ), 9),
                "Wizard": ("None", 5),
            },
        ),
    },
    "Feats": {
        "Vital Sacrifice": (Damage_Type.NECROTIC),
        "Gift of the Chromatic Dragon": (
            Damage_Type.ACID,
            Damage_Type.COLD,
            Damage_Type.FIRE,
            Damage_Type.LIGHTNING
        ),
    },
    "Species": {
        "Aasimar": (
            Damage_Type.NECROTIC,
            Damage_Type.RADIANT,
        ),
        "Giff": (Damage_Type.FORCE),
    },
}

official_sources_with_damage_options = {
    "Background": {
        "Strike of the Giants": (
            Damage_Type.COLD,
            Damage_Type.FIRE,
            Damage_Type.FORCE,
            Damage_Type.LIGHTNING,
            Damage_Type.THUNDER,
        ),
    },
    "Classes": {
        "Blood Hunter": {
            "None_2": ((
                Damage_Type.COLD,
                Damage_Type.FIRE,
                Damage_Type.LIGHTNING
            ), 2),
        },
        "Cleric": {
            "Nature": ((
                Damage_Type.COLD,
                Damage_Type.FIRE,
                Damage_Type.LIGHTNING,
            ), 8)
        },
    },
    "Concentration": {
        "Elemental Weapon": (
            (
                Damage_Type.ACID,
                Damage_Type.COLD,
                Damage_Type.FIRE,
                Damage_Type.LIGHTNING,
                Damage_Type.THUNDER
            ), {
                "Artificer": ("None", 9),
                "Cleric": ("Forge", 5),
                "Paladin": ("None", 9),
            },
        ),
        "Spirit Shroud": (
            (
                Damage_Type.COLD,
                Damage_Type.NECROTIC,
                Damage_Type.RADIANT,
            ), {
                "Cleric": ("None", 5),
                "Paladin": ("None", 9),
                "Warlock": ("None", 5),
                "Wizard": ("None", 5),
            },
        ),
    },
    "Feats": {
        "Gift of the Chromatic Dragon": (
            Damage_Type.ACID,
            Damage_Type.COLD,
            Damage_Type.FIRE,
            Damage_Type.LIGHTNING,
        ),
    },
    "Species": {
        "Aasimar": (
            Damage_Type.NECROTIC,
            Damage_Type.RADIANT,
        ),
    }
}
