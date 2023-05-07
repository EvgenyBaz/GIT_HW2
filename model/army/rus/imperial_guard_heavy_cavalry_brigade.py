from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.cavalry.life_guard_cuirassier import LifeGuardCuirassier
from model.army.rus.cavalry.chevalier_guard import ChevalierGuard
from model.army.rus.cavalry.life_guard_horse import LifeGuardHorse
from model.army.rus.artilllery.guard_horse_artillery_battery import GuardHorseArtilleryBattery
from model.army.rus.artilllery.guard_horse_artillery_half_battery import GuardHorseArtilleryHalfBattery

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8
class LifeGuadHeavyCavalryBrigade(Brigade):

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
        self.brigade_list_battalion_list.append(self.first_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Large", 8])
        self.brigade_bonus_list.append(["Small", -8])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Large": [LifeGuardCuirassier.get_name_of_battalion(),
                       ChevalierGuard.get_name_of_battalion(),
                       LifeGuardHorse.get_name_of_battalion()],
             "Small": [LifeGuardCuirassier.get_name_of_battalion(),
                       ChevalierGuard.get_name_of_battalion(),
                       LifeGuardHorse.get_name_of_battalion()]
             }

    def main_battalion_list(self):
        return [
            Unit(),
            LifeGuardCuirassier(),
            ChevalierGuard(),
            LifeGuardHorse(),
            GuardHorseArtilleryBattery(),
            GuardHorseArtilleryHalfBattery()
        ]
    def first_battalion_list(self):
        return [
            Unit(),
            LifeGuardCuirassier(),
            ChevalierGuard(),
            LifeGuardHorse()
        ]

