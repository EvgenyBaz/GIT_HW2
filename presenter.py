from module.army.rus.infantry_brigade import InfantryBrigade
class Presenter():
    def __init__(self):
        self.rusInfantryBrigade = []
    def rusLineInfantryBrigadeCorrList(self):
        self.rusInfantryBrigade = InfantryBrigade().get_list_of_infantry_brigade()
        return self.rusInfantryBrigade
