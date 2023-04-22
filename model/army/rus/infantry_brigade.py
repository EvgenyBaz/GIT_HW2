from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.infantry.line_Infantry import LineInfantry
from model.army.rus.infantry.combined_grenadier import CombinedGrenadier
from model.army.rus.infantry.opolchenie_pike import OpolcheniePike
from model.army.rus.infantry.opolchenie_musket import OpolchenieMusket
from model.army.rus.infantry.opolchenie_jager import OpolchenieJager
from model.army.rus.infantry.volunteer_jager_musket import VolunteerJagerMusket
from model.army.rus.infantry.volunteer_jager_rifle import VolunteerJagerRifle
from model.army.rus.infantry.jager import Jager
from model.army.rus.infantry.jager_two_battalions import JagerTwoBattalions

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8


class InfantryBrigade(Brigade):

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
        self.brigade_list.append(Unit())  # дополнительный батальон

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.brigade_list_battalion_list.append(
            self.additional_battalion_list())  # дополнительный батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Veteran", 8])
        self.brigade_bonus_list.append(["Small", -8])
        self.brigade_bonus_list.append(["Sharpshooter", 3])
        self.brigade_bonus_list.append(["Veteran regiment", 16])
        self.brigade_bonus_list.append(["Small regiment", -16])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Veteran": [LineInfantry.get_name_of_battalion(),
                         CombinedGrenadier.get_name_of_battalion(),
                         Jager.get_name_of_battalion(),
                         VolunteerJagerRifle.get_name_of_battalion(),
                         VolunteerJagerMusket.get_name_of_battalion()],
             "Small": [LineInfantry.get_name_of_battalion(),
                       CombinedGrenadier.get_name_of_battalion(),
                       Jager.get_name_of_battalion(),
                       OpolcheniePike.get_name_of_battalion(),
                       OpolchenieMusket.get_name_of_battalion(),
                       OpolchenieJager.get_name_of_battalion(),
                       VolunteerJagerRifle.get_name_of_battalion(),
                       VolunteerJagerMusket.get_name_of_battalion()],
             "Sharpshooter": [VolunteerJagerRifle.get_name_of_battalion(),
                              VolunteerJagerMusket.get_name_of_battalion()],
             "Veteran regiment": [JagerTwoBattalions.get_name_of_battalion()],
             "Small regiment": [JagerTwoBattalions.get_name_of_battalion()]
             }


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


