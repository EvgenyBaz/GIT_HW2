from module.army.rus.infantry_brigade import InfantryBrigade
class Presenter():
    def __init__(self):
        self.rusInfantryBrigade = []
    def rusLineInfantryBrigadeCoreList(self):
        self.rusInfantryBrigade = InfantryBrigade().get_list_of_infantry_brigade()
        return self.rusInfantryBrigade

    def rusLineInfantryBrigadeAddList(self):
        self.rusInfantryBrigade = InfantryBrigade().get_additional_list_of_infantry_brigade()
        return self.rusInfantryBrigade