from module.army.unit import Unit
from module.army.rus.infantry.line_Infantry import LineInfantry
from module.army.rus.infantry.combined_grenadier import CombinedGrenadier
from module.army.rus.infantry.opolchenie_pike import OpolcheniePike
from module.army.rus.infantry.opolchenie_musket import OpolchenieMusket
from module.army.rus.infantry.opolchenie_jager import OpolchenieJager
from module.army.rus.infantry.volunteer_jager_musket import VolunteerJagerMusket
from module.army.rus.infantry.volunteer_jager_rifle import VolunteerJagerRifle
from module.army.rus.infantry.jager import Jager
from module.army.rus.infantry.jager_two_battalions import JagerTwoBattalions

from module.army.rus.commanders.commander_skill7 import CommanderSkill7
from module.army.rus.commanders.commander_skill8 import CommanderSkill8


class InfantryBrigade:

    def __init__(self):
        # список командиров
        self.infantry_brigade_commanders_list = []
        self.infantry_brigade_commanders_list.append(CommanderSkill7())
        self.infantry_brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.infantry_brigade_list = []
        self.infantry_brigade_list.append(Unit())  # первый батальон
        self.infantry_brigade_list.append(Unit())  # второй батальон
        self.infantry_brigade_list.append(Unit())  # третий батальон
        self.infantry_brigade_list.append(Unit())  # четвертый батальон
        self.infantry_brigade_list.append(Unit())  # дополнительный батальон

        # возможные вариации для каждого батальона
        self.infantry_brigade_list_battalion_list = []
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.infantry_brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.infantry_brigade_list_battalion_list.append(
            self.additional_battalion_list())  # дополнительный батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.infantry_brigade_bonus_list = []
        self.infantry_brigade_bonus_list.append(["Veteran", 8])
        self.infantry_brigade_bonus_list.append(["Small", -8])
        self.infantry_brigade_bonus_list.append(["Sharpshooter", 3])

        # зададим сллтветствие бонусу - батальона
        self.infantry_brigade_bonus_battalion_correspondence = {}
        self.infantry_brigade_bonus_battalion_correspondence = \
            {"Veteran": [LineInfantry.get_class_name_of_battalion(),
                         CombinedGrenadier.get_class_name_of_battalion(),
                         Jager.get_class_name_of_battalion(),
                         JagerTwoBattalions.get_class_name_of_battalion(),
                         VolunteerJagerRifle.get_class_name_of_battalion(),
                         VolunteerJagerMusket.get_class_name_of_battalion()],
             "Small": [LineInfantry.get_class_name_of_battalion(),
                       CombinedGrenadier.get_class_name_of_battalion(),
                       Jager.get_class_name_of_battalion(),
                       JagerTwoBattalions.get_class_name_of_battalion(),
                       OpolcheniePike.get_class_name_of_battalion(),
                       OpolchenieMusket.get_class_name_of_battalion(),
                       OpolchenieJager.get_class_name_of_battalion(),
                       VolunteerJagerRifle.get_class_name_of_battalion(),
                       VolunteerJagerMusket.get_class_name_of_battalion()],
             "Sharpshooter": [VolunteerJagerRifle.get_class_name_of_battalion(),
                              VolunteerJagerMusket.get_class_name_of_battalion()]
             }

    def get_infantry_brigade_bonus_to_battalion_list(self, bonus_name):
        return self.infantry_brigade_bonus_battalion_correspondence[bonus_name]

    def get_infantry_brigade_bonus_list_names(self):
        bonus_names_list = []
        for i in range(len(self.infantry_brigade_bonus_list)):
            bonus_names_list.append(self.infantry_brigade_bonus_list[i][0])
        return bonus_names_list

    def get_infantry_brigade_bonus_list_costs(self):
        bonus_cost_list = []
        for i in range(len(self.infantry_brigade_bonus_list)):
            bonus_cost_list.append(self.infantry_brigade_bonus_list[i][1])
        return bonus_cost_list

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
            Unit(),
            LineInfantry()
        ]

    def additional_battalion_list(self):
        return [
            Unit(),
            CombinedGrenadier(),
            OpolcheniePike(),
            OpolchenieMusket(),
            OpolchenieJager(),
            VolunteerJagerMusket(),
            VolunteerJagerRifle(),
            Jager(),
            JagerTwoBattalions()
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
        return self.infantry_brigade_list[order_number].cost + self.infantry_brigade_list[order_number].bonus_cost

    def get_name_of_battalion(self, order_number):
        return self.infantry_brigade_list[order_number].name

    # добавляем свойство в список бонусов батальона
    def set_battalion_bonus(self, bonus, order_number):
        self.infantry_brigade_list[order_number].bonus[bonus] = None

    def del_battalion_bonus(self, bonus, order_number):
        del self.infantry_brigade_list[order_number].bonus[bonus]

    # добавляем стоимость бонуса к общей стоимости бонусов батальона
    def add_bonus_cost_to_battalion(self, new_bonus_cost, order_number):
        self.infantry_brigade_list[order_number].bonus_cost += new_bonus_cost

    # возвращаем по запросу список всех бонусов батальона
    def get_bonus_list(self, order_number):
        return self.infantry_brigade_list[order_number].bonus
