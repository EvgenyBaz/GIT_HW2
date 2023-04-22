from model.army.rus.rus_corps import RusCorps

class Presenter():
    def __init__(self, country):
    #производим выбок структуры и наполнения корпуса в зависимости от выбранной  страны
        if country =="Rus":
            self.corps = RusCorps()

    # запрос на список имен батальонов
    def BrigadeBttlnList(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_list_battalion_names(order_number)

        # отправляет данные в модель для заполнения списка бригады
    def BrigadeBttlnChoosen(self, order_number, bttln_choosen_from_list, brigade_number):
        return self.corps.get_brigade(brigade_number).set_battalion_to_list(order_number, bttln_choosen_from_list)

    # запрос на стоимость текущего батальона
    def BrigadeBttlnCost(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_cost_of_battalion(order_number)

    # запрос имени текущего батальона
    def BrigadeBttlnName(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_name_of_battalion(order_number)

    #запрос на список бонусов для бригады
    def BrigadeBonusNameList(self,brigade_number):
        return self.corps.get_brigade(brigade_number).get_brigade_bonus_list_names()

    # def BrigadeBonusNameList(self, order_number, brigade_number):
    #     return self.corps.get_brigade(brigade_number).get_brigade_bonus_list_names()[order_number]

    # запрос на список стоимости бонусов для бригады
    def BrigadeBonusCostList(self, brigade_number):
        return self.corps.get_brigade(brigade_number).get_brigade_bonus_list_costs()

    def BrigadeBonusToBattalion(self, bonus_name, brigade_number):
        return self.corps.get_brigade(brigade_number).get_brigade_bonus_to_battalion_list(bonus_name)

    # отправляем добавление бонуса к батальону
    def BrigadeBttlnBonusAdd(self, bonus, order_number, brigade_number):
        self.corps.get_brigade(brigade_number).set_battalion_bonus(bonus, order_number)

    # отправляем удаление бонуса у батальона
    def BrigadeBttlnBonusDel(self, bonus, order_number, brigade_number):
        self.corps.get_brigade(brigade_number).del_battalion_bonus(bonus, order_number)

    # отправляем стоимомть бонуса для батальона
    def BrigadeBttlnBonusCostAdd(self, bonus_cost, order_number, brigade_number):
        self.corps.get_brigade(brigade_number).add_bonus_cost_to_battalion(bonus_cost, order_number)

    # запрашиваем список бонусов батальона
    def BrigadeBttlnBonusList(self, order_number, brigade_number):
        return self.corps.get_brigade(brigade_number).get_bonus_list(order_number)

    # запрашивает список имен командиров
    def BrigadeCmndrsNamesList(self, brigade_number):
        return self.corps.get_brigade(brigade_number).get_list_commanders_names()

    # запрашивает стоимость выбранного командира
    def BrigadeCmndrsCost(self, index, brigade_number):
        return self.corps.get_brigade(brigade_number).get_costs_of_commander(index)

    # запрашивает список имен командиров для корпуса
    def CorpsCmndrsNamesList(self):
        return self.corps.get_list_commanders_names()

    # запрашивает стоимость выбранного командира
    def CorpsCmndrsCost(self, index):
        return self.corps.get_costs_of_commander(index)