from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.infantry.jager import Jager
from model.army.rus.infantry.grenadier import Grenadier

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8

class JagerBrigade(Brigade):

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
        self.brigade_list.append(Unit())  # четвертый батальон
        self.brigade_list.append(Unit())  # пятый батальон
        self.brigade_list.append(Unit())  # шестой батальон
        self.brigade_list.append(Unit())  # дополнительный первый батальон
        self.brigade_list.append(Unit())  # дополнительный второй батальон

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # пятый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # шестой батальон - варианты
        self.brigade_list_battalion_list.append(
            self.additional_battalion_list())  # первый дополнительный батальон - варианты
        self.brigade_list_battalion_list.append(
            self.additional_battalion_list())  # второй дополнительный батальон - варианты


        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Veteran", 8])
        self.brigade_bonus_list.append(["Small", -8])
        self.brigade_bonus_list.append(["None", 0])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [Jager.get_name_of_battalion()],
             "Small": [Jager.get_name_of_battalion()],
             "None": []
             }


    def main_battalion_list(self):
        return [
            Unit(),
            Jager()
        ]

    def additional_battalion_list(self):
        return [
            Unit(),
            Grenadier()
        ]