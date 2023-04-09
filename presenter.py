from module.army.rus.infantry_brigade import InfantryBrigade


class Presenter():
    def __init__(self):
        self.infantry_brigade = InfantryBrigade()

    # запрос на список имен батальонов
    def rusLineInfantryBrigadeBttlnList(self, order_number):
        return self.infantry_brigade.get_list_battalion_names(order_number)

        # отправляет данные в модель для заполнения списка бригады
    def rusLineInfantryBrigadeBttlnChoosen(self, order_number, bttln_choosen_from_list):
        self.infantry_brigade.set_battalion_to_list (order_number, bttln_choosen_from_list)

# запрос на стоимость текущего батальона
    def rusLineInfantryBrigadeBttlnCost(self, order_number):
        return self.infantry_brigade.get_cost_of_battalion(order_number)

# запрос имени текущего батальона
    def rusLineInfantryBrigadeBttlnName(self, order_number):
        return self.infantry_brigade.get_name_of_battalion(order_number)
