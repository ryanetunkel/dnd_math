"""The Dnd_Class Class"""

from class_type import Class_Type
from dnd_subclass import Dnd_Subclass

class Dnd_Class():
    def __init__(self, _class_type:Class_Type, _level:int):
        self._class_type = _class_type
        self._level = _level
        self.class_name = str(_class_type.name).title()
        self.subclass = Dnd_Subclass(_class_type.value,self._level)
        self.subclass_options = self.subclass.subclass_options
# TODO: Add in clause for taking a class not including a subclass,
# make sure to leave option for picking subclass in future and that
# picking one but getting somethign else that also has it doesn't override
# it in case that prevents from taking the other