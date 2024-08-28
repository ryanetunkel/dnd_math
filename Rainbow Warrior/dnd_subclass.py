"""The Dnd_Subclass Class"""

from class_type import Class_Type
from damage_type import Damage_Type

class Dnd_Subclass():
    def __init__(self, _class_type:int, _level:int):
        self._class_type = _class_type
        self._level = _level
        self.subclass_options = {}
        self.subclass_name = "" # Is interim value. An actual class with no given subclass has the subclass "None"
        match self._class_type:
            case Class_Type.NONE:
                self.subclass_options = {}
            case Class_Type.ARTIFICER:
                self.subclass_options = {"Battle_Smith": ((Damage_Type.FORCE), 9),} if self._level >= 9 else {}
            case Class_Type.BARD:
                self.subclass_options = {
                    "Creation": ((Damage_Type.THUNDER), 3),
                    "Whispers": ((Damage_Type.PSYCHIC), 3),
                    } if self._level >= 3 else {}
            case Class_Type.BLOOD_HUNTER:
                self.subclass_options = {"Ghostslayer": ((Damage_Type.RADIANT), 3),} if self._level >= 3 else {}
            case Class_Type.CLERIC:
                if self._level >= 8:
                    self.subclass_options = {
                        "Death": ((Damage_Type.NECROTIC), 2),
                        "Forge": ((Damage_Type.FIRE), 8),
                        "Life": ((Damage_Type.RADIANT), 8),
                        "Nature": ((Damage_Type.COLD,Damage_Type.FIRE,Damage_Type.LIGHTNING), 8),
                        "Order": ((Damage_Type.PSYCHIC), 8),
                        "Tempest": ((Damage_Type.THUNDER), 8),
                        "Twilight": ((Damage_Type.RADIANT), 8),
                    }
                elif 8 > self._level >= 2:
                    self.subclass_options = {"Death": ((Damage_Type.NECROTIC), 2),}
                else: self.subclass_options = {}
            case Class_Type.DRUID:
                self.subclass_options = {"Spores": ((Damage_Type.NECROTIC), 2),} if self._level >= 2 else {}
            case Class_Type.FIGHTER:
                self.subclass_options = {
                    "Psionic": ((Damage_Type.FORCE), 3),
                    "Rune": ((Damage_Type.FIRE), 3),
                } if self._level >= 3 else {}
            case Class_Type.PALADIN:
                self.subclass_options = {}
            case Class_Type.RANGER:
                self.subclass_options = {"Swarmkeeper": ((Damage_Type.PIERCING), 3),} if self._level >= 3 else {}
            case Class_Type.WARLOCK:
                self.subclass_options = {"Genie": ((Damage_Type.BLUDGEONING), 1),} if self._level >= 1 else {}
# TODO: Add in functions for selecting subclass
