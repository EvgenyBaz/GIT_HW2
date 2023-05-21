from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.ita.cavalry.italian_chasseurs_a_cheval import ItalianChasseursACheval

from model.army.basic_commander import BasicCommander
from model.army.ita.commanders.commander_skill7 import CommanderSkill7
from model.army.ita.commanders.commander_skill8 import CommanderSkill8

class CavalryBrigade(Brigade):

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

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Veteran", 6])
        self.brigade_bonus_list.append(["Small", -8])
        self.brigade_bonus_list.append(["Wavering", -6])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [ItalianChasseursACheval.get_name_of_battalion()],
             "Small": [ItalianChasseursACheval.get_name_of_battalion()],
             "Wavering": [ItalianChasseursACheval.get_name_of_battalion()]
             }

    def main_battalion_list(self):
        return [
            Unit(),
            ItalianChasseursACheval(),

        ]


