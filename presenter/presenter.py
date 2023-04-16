from model.army.rus.infantry_brigade import InfantryBrigade
from model.army.rus.corps import Corps

class Presenter():
    def __init__(self):
        self.corps = Corps()

    # запрос на список имен батальонов
    def rusLineInfantryBrigadeBttlnList(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_list_battalion_names(order_number)

        # отправляет данные в модель для заполнения списка бригады
    def rusLineInfantryBrigadeBttlnChoosen(self, order_number, bttln_choosen_from_list, brigade_number):
        return self.corps.get_brigade(brigade_number).set_battalion_to_list(order_number, bttln_choosen_from_list)

    # запрос на стоимость текущего батальона
    def rusLineInfantryBrigadeBttlnCost(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_cost_of_battalion(order_number)

    # запрос имени текущего батальона
    def rusLineInfantryBrigadeBttlnName(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_name_of_battalion(order_number)

    #запрос на список бонусов для бригады
    def rusLineInfantryBrigadeBonusNameList(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_infantry_brigade_bonus_list_names()[order_number]

    # запрос на список стоимости бонусов для бригады
    def rusLineInfantryBrigadeBonusCostList(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_infantry_brigade_bonus_list_costs()[order_number]

    def rusLineInfantryBrigadeBonusToBattalion(self, bonus_name, brigade_number):
        return self.corps.get_brigade(brigade_number).get_infantry_brigade_bonus_to_battalion_list(bonus_name)

    # отправляем добавление бонуса к батальону
    def rusLineInfantryBrigadeBttlnBonusAdd(self, bonus, order_number, brigade_number):
        self.corps.get_brigade(brigade_number).set_battalion_bonus(bonus, order_number)

    # отправляем удаление бонуса у батальона
    def rusLineInfantryBrigadeBttlnBonusDel(self, bonus, order_number, brigade_number):
        self.corps.get_brigade(brigade_number).del_battalion_bonus(bonus, order_number)

    # отправляем стоимомть бонуса для батальона
    def rusLineInfantryBrigadeBttlnBonusCostAdd(self, bonus_cost, order_number, brigade_number):
        self.corps.get_brigade(brigade_number).add_bonus_cost_to_battalion(bonus_cost, order_number)

    # запрашиваем список бонусов батальона
    def rusLineInfantryBrigadeBttlnBonusList(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_bonus_list(order_number)

    # запрашивает список имен командиров
    def rusLineInfantryBrigadeCmndrsNamesList(self, brigade_number):
        return self.corps.get_brigade(brigade_number).get_list_commanders_names()

    # запрашивает стоимость выбранного командира
    def rusLineInfantryBrigadeCmndrsCost(self, index, brigade_number):
        return self.corps.get_brigade(brigade_number).get_costs_of_commander(index)

    # запрашивает список имен командиров для корпуса
    def rusCorpsCmndrsNamesList(self):
        return self.corps.get_list_commanders_names()

    # запрашивает стоимость выбранного командира
    def rusCorpsCmndrsCost(self, index):
        return self.corps.get_costs_of_commander(index)