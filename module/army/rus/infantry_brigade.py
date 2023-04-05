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

        self.additional_infantry_brigade_list = [
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
        return self.infantry_brigade_list

    def get_additional_list_of_infantry_brigade(self):
        return self.additional_infantry_brigade_list
