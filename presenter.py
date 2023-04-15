from module.army.rus.infantry_brigade import InfantryBrigade


class Presenter():
    def __init__(self):
        self.infantry_brigade = InfantryBrigade()

    # запрос на список имен батальонов
    def rusLineInfantryBrigadeBttlnList(self, order_number):
        return self.infantry_brigade.get_list_battalion_names(order_number)

        # отправляет данные в модель для заполнения списка бригады

    def rusLineInfantryBrigadeBttlnChoosen(self, order_number, bttln_choosen_from_list):
        self.infantry_brigade.set_battalion_to_list(order_number, bttln_choosen_from_list)

    # запрос на стоимость текущего батальона
    def rusLineInfantryBrigadeBttlnCost(self, order_number):
        return self.infantry_brigade.get_cost_of_battalion(order_number)

    # запрос имени текущего батальона
    def rusLineInfantryBrigadeBttlnName(self, order_number):
        return self.infantry_brigade.get_name_of_battalion(order_number)

    # отправляем добавление бонуса к батальону
    def rusLineInfantryBrigadeBttlnBonusAdd(self, bonus, order_number):
        self.infantry_brigade.set_battalion_bonus(bonus, order_number)

    # отправляем удаление бонуса у батальона
    def rusLineInfantryBrigadeBttlnBonusDel(self, bonus, order_number):
        self.infantry_brigade.del_battalion_bonus(bonus, order_number)

    # отправляем стоимомть бонуса для батальона
    def rusLineInfantryBrigadeBttlnBonusCostAdd(self, bonus_cost, order_number):
        self.infantry_brigade.add_bonus_cost_to_battalion(bonus_cost, order_number)

    # запрашиваем список бонусов батальона
    def rusLineInfantryBrigadeBttlnBonusList(self, order_number):
        return self.infantry_brigade.get_bonus_list(order_number)

    # запрашивает список имен командиров
    def rusLineInfantryBrigadeCmndrsNamesList(self):
        return self.infantry_brigade.get_list_commanders_names()

    # запрашивает стоимость выбранного командира
    def rusLineInfantryBrigadeCmndrsCost(self, index):
        return self.infantry_brigade.get_costs_of_commander(index)
