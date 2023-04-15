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
from module.army.rus.commanders import commander_skill7
from module.army.rus.commanders import commander_skill8


class InfantryBrigade:

    def __init__(self):
        # список командиров
        self.infantry_brigade_commanders_list = []
        self.infantry_brigade_commanders_list.append(commander_skill7.CommanderSkill7())
        self.infantry_brigade_commanders_list.append(commander_skill8.CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.infantry_brigade_list = []
        self.infantry_brigade_list.append(unit.Unit())  # первый батальон
        self.infantry_brigade_list.append(unit.Unit())  # второй батальон
        self.infantry_brigade_list.append(unit.Unit())  # третий батальон
        self.infantry_brigade_list.append(unit.Unit())  # четвертый батальон
        self.infantry_brigade_list.append(unit.Unit())  # дополнительный батальон

        # возможные вариации для каждого батальона
        self.infantry_brigade_list_battalion_list = []
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.infantry_brigade_list_battalion_list.append(
            self.additional_battalion_list())  # дополнительный батальон - варианты


    def get_list_commanders_names(self):
        infantry_brigade_cmndrs_names = []
        for cmndr in self.infantry_brigade_commanders_list:
            infantry_brigade_cmndrs_names.append(cmndr.get_name_of_commander())
        return infantry_brigade_cmndrs_names

# по порядковому номеру в списке командиров возвращает его стоимость
    def get_costs_of_commander(self, index):
        return self.infantry_brigade_commanders_list[index].get_cost_of_commander()

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

    # создает список имен батальонов в зависимости от порядкового номера батальона в бригаде
    def get_list_battalion_names(self, order_number):
        infantry_brigade_bttln_list_names = []

        for bttln in self.infantry_brigade_list_battalion_list[order_number]:
            infantry_brigade_bttln_list_names.append(bttln.name)
        return infantry_brigade_bttln_list_names

    # помещает выбраный в интерфейсе батальон (обьект) в список бригады на позицию соответствующую кнопке
    def set_battalion_to_list(self, order_number, bttln_choosen_from_list):
        self.infantry_brigade_list[order_number] = self.infantry_brigade_list_battalion_list[order_number][
            bttln_choosen_from_list]

    def get_cost_of_battalion(self, order_number):
        return self.infantry_brigade_list[order_number].cost+self.infantry_brigade_list[order_number].bonus_cost

    def get_name_of_battalion(self, order_number):
        return self.infantry_brigade_list[order_number].name
    # добавляем свойство в список бонусов батальона
    def set_battalion_bonus(self, bonus, order_number):
        self.infantry_brigade_list[order_number].bonus[bonus]=None

    def del_battalion_bonus(self, bonus, order_number):
        del self.infantry_brigade_list[order_number].bonus[bonus]
    # добавляем стоимость бонуса к общей стоимости бонусов батальона
    def add_bonus_cost_to_battalion(self, new_bonus_cost, order_number):
        self.infantry_brigade_list[order_number].bonus_cost += new_bonus_cost
    # возвращаем по запросу список всех бонусов батальона
    def get_bonus_list(self, order_number):
        return self.infantry_brigade_list[order_number].bonus
