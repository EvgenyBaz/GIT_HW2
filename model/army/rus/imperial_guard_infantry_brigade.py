from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.infantry.life_guard_infantry import LifeGuardInfantry
from model.army.rus.infantry.life_guard_jager import LifeGuardJager
from model.army.rus.artilllery.guard_light_artillery_battery import GuardLightArtilleryBattery
from model.army.rus.artilllery.guard_light_artillery_half_battery import GuardLightArtilleryHalfBattery
from model.army.rus.artilllery.guard_position_artillery_battery import GuardPositionArtilleryBattery
from model.army.rus.artilllery.guard_position_artillery_half_battery import GuardPositionArtilleryHalfBattery

from model.army.basic_commander import BasicCommander
from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8

class LifeGuardInfantryBrigade(Brigade):

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
        self.brigade_list.append(Unit())  # дополнительная рота легкой артиллерии
        self.brigade_list.append(Unit())  # дополнительная рота тяжелой артиллерии

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # первый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # второй батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # третий батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # четвертый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # пятый батальон - варианты
        self.brigade_list_battalion_list.append(self.main_battalion_list())  # шестой батальон - варианты
        self.brigade_list_battalion_list.append(
            self.additional_light_artillery_list())  # дополнительная легкая батарея - варианты
        self.brigade_list_battalion_list.append(
            self.additional_heavy_artillery_list())  # дополнительная тяжелая батарея - варианты

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []
        self.brigade_bonus_list.append(["Small", -8])

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}
        self.brigade_bonus_battalion_correspondence = \
            {"Small": [LifeGuardInfantry.get_name_of_battalion(),
                       LifeGuardJager.get_name_of_battalion()]
             }

    def main_battalion_list(self):
        return [
            Unit(),
            LifeGuardInfantry(),
            LifeGuardJager()
        ]

    def additional_light_artillery_list(self):
        return [
            Unit(),
            GuardLightArtilleryBattery(),
            GuardLightArtilleryHalfBattery()
        ]

    def additional_heavy_artillery_list(self):
        return [
            Unit(),
            GuardPositionArtilleryBattery(),
            GuardPositionArtilleryHalfBattery()
        ]
