from module.army.rus.infantry import line_Infantry
from module.army.rus.infantry import combined_grenadier
from module.army.rus.infantry import opolchenie_pike
from module.army.rus.infantry import opolchenie_musket
from module.army.rus.infantry import opolchenie_jager
from module.army.rus.infantry import volunteer_jager_musket
from module.army.rus.infantry import volunteer_jager_rifle
from module.army.rus.infantry import jager
from module.army.rus.infantry import jager_two_battalions
from module.army import unit


class InfantryBrigade:

    def __init__(self):
        self.infantry_brigade_list = [
            unit.Unit(),
            line_Infantry.LineInfantry()
        ]
        self.infantry_brigade_list_names=[]

        self.additional_infantry_brigade_list = [
            unit.Unit(),
            combined_grenadier.CombinedGrenadier(),
            opolchenie_pike.OpolcheniePike(),
            opolchenie_musket.OpolchenieMusket(),
            opolchenie_jager.OpolchenieJager(),
            volunteer_jager_musket.VolunteerJagerMusket(),
            volunteer_jager_rifle.VolunteerJagerRifle(),
            jager.Jager(),
            jager_two_battalions.JagerTwoBattalions()
        ]

    def get_list_of_infantry_brigade(self):

        for btln in self.infantry_brigade_list:
            self.infantry_brigade_list_names.append(btln.name)
        return self.infantry_brigade_list_names

    def get_additional_list_of_infantry_brigade(self):

        for btln in self.additional_infantry_brigade_list:
            self.infantry_brigade_list_names.append(btln.name)
        return self.infantry_brigade_list_names

