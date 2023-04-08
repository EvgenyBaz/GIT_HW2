from module.army.rus.infantry_brigade import InfantryBrigade
class Presenter():
    def __init__(self):
        # self.rusInfantryBrigade1stBthn = []
        # self.rusInfantryBrigade2ndBthn = []
        # self.rusInfantryBrigade3rdBthn = []
        # self.rusInfantryBrigade4thBthn = []
        self.infantry_brigade = InfantryBrigade()
    def rusLineInfantryBrigade1stBttlnList(self):
        return self.infantry_brigade.get_list_of_first_battalion_names()
    def rusLineInfantryBrigade1stBttlnCost(self, index):
        return self.infantry_brigade.get_cost_of_first_battalion(index)

    def rusLineInfantryBrigade2ndBttlnList(self):
        return self.infantry_brigade.get_list_of_second_battalion_names()

    def rusLineInfantryBrigade2ndBttlnCost(self, index):
        return self.infantry_brigade.get_cost_of_second_battalion(index)
    def rusLineInfantryBrigade3rdBttlnList(self):
        return self.infantry_brigade.get_list_of_third_battalion_names()

    def rusLineInfantryBrigade3rdBttlnCost(self, index):
        return self.infantry_brigade.get_cost_of_third_battalion(index)

    def rusLineInfantryBrigade4thBttlnList(self):
        return self.infantry_brigade.get_list_of_fourth_battalion_names()

    def rusLineInfantryBrigade4thBttlnCost(self, index):
        return self.infantry_brigade.get_cost_of_fourth_battalion(index)

    def rusLineInfantryBrigadeAddList(self):
        return self.infantry_brigade.get_additional_list_of_battalion_names()

    def rusLineInfantryBrigadeAddBttlnCost(self, index):
        return self.infantry_brigade.get_cost_of_additional_battalion(index)