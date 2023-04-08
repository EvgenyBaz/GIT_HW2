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

        # self.infantry_brigade_list_names=[]

        self.infantry_brigade_first_battalion_list = self.main_battalion_list()
        self.infantry_brigade_second_battalion_list = self.main_battalion_list()
        self.infantry_brigade_third_battalion_list = self.main_battalion_list()
        self.infantry_brigade_fourth_battalion_list = self.main_battalion_list()
        self.infantry_brigade_additional_battalion_list = self.additional_battalion_list()

        # self.additional_infantry_brigade_list =
    def main_battalion_list(self):

        return [
            unit.Unit(),
            line_Infantry.LineInfantry()
        ]

    def additional_battalion_list(self):
        return [
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

    def get_list_of_first_battalion_names(self):
        infantry_brigade_list_names = []
        for bttln in self.infantry_brigade_first_battalion_list:
            infantry_brigade_list_names.append(bttln.name)
        return infantry_brigade_list_names

    def get_cost_of_first_battalion(self, index):
        infantry_battalion_cost = []
        for bttln in self.infantry_brigade_first_battalion_list:
            infantry_battalion_cost.append(bttln.cost)
        return infantry_battalion_cost[index]

    def get_list_of_second_battalion_names(self):
        infantry_brigade_list_names = []
        for bttln in self.infantry_brigade_second_battalion_list:
            infantry_brigade_list_names.append(bttln.name)
        return infantry_brigade_list_names

    def get_cost_of_second_battalion(self, index):
        infantry_battalion_cost = []
        for bttln in self.infantry_brigade_second_battalion_list:
            infantry_battalion_cost.append(bttln.cost)
        return infantry_battalion_cost[index]

    def get_list_of_third_battalion_names(self):
        infantry_brigade_list_names = []
        for bttln in self.infantry_brigade_third_battalion_list:
            infantry_brigade_list_names.append(bttln.name)
        return infantry_brigade_list_names

    def get_cost_of_third_battalion(self, index):
        infantry_battalion_cost = []
        for bttln in self.infantry_brigade_third_battalion_list:
            infantry_battalion_cost.append(bttln.cost)
        return infantry_battalion_cost[index]

    def get_list_of_fourth_battalion_names(self):
        infantry_brigade_list_names = []
        for bttln in self.infantry_brigade_first_battalion_list:
            infantry_brigade_list_names.append(bttln.name)
        return infantry_brigade_list_names

    def get_cost_of_fourth_battalion(self, index):
        infantry_battalion_cost = []
        for bttln in self.infantry_brigade_fourth_battalion_list:
            infantry_battalion_cost.append(bttln.cost)
        return infantry_battalion_cost[index]

    def get_additional_list_of_battalion_names(self):
        infantry_brigade_list_names = []
        for bttln in self.infantry_brigade_additional_battalion_list:
            infantry_brigade_list_names.append(bttln.name)
        return infantry_brigade_list_names

    def get_cost_of_additional_battalion(self, index):
        infantry_battalion_cost = []
        for bttln in self.infantry_brigade_additional_battalion_list:
            infantry_battalion_cost.append(bttln.cost)
        return infantry_battalion_cost[index]

