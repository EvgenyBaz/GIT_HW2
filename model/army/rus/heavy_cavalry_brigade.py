from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.cavalry.dragoon import Dragoon
from model.army.rus.infantry.dragoon_on_foot import DragoonOnFoot
from model.army.rus.cavalry.cuirassier import Cuirassier


from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8


class HeavyCavalryBrigade(Brigade):

    def __init__(self):
        # список командиров
        self.brigade_commanders_list = []
        self.brigade_commanders_list.append(BasicCommander())
        self.brigade_commanders_list.append(CommanderSkill7())
        self.brigade_commanders_list.append(CommanderSkill8())

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list = []
        self.brigade_list.append(Unit())  # первый батальон
        self.brigade_list.append(Unit())  # второй батальон
        self.brigade_list.append(Unit())  # третий батальон

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.third_battalion_list())  # третий батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Veteran", 6])
        self.brigade_bonus_list.append(["Large", 8])
        self.brigade_bonus_list.append(["Small", -8])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [Dragoon.get_name_of_battalion(),
                         DragoonOnFoot.get_name_of_battalion(),
                         Cuirassier.get_name_of_battalion()],
             "Large": [Dragoon.get_name_of_battalion(),
                         Cuirassier.get_name_of_battalion()],
             "Small": [Dragoon.get_name_of_battalion(),
                         Cuirassier.get_name_of_battalion()]
             }

    def main_battalion_list(self):
        return [
            Unit(),
            Dragoon(),
            DragoonOnFoot(),
            Cuirassier()
        ]

    def third_battalion_list(self):
        return [
            Unit(),
            Dragoon(),
            DragoonOnFoot()
        ]



    def set_common_list_of_battalions(self, order_number):
        self.brigade_list_battalion_list[order_number].insert(0, Unit())
    def set_list_of_battalions(self, order_number):
        self.brigade_list_battalion_list[order_number].pop(0)