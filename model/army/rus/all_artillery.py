from model.army.brigade import Brigade

from model.army.unit import Unit
from model.army.rus.artilllery.light_artillery_battery import Light_Artillery_Battery
from model.army.rus.artilllery.light_artillery_half_battery import Light_Artillery_Half_Battery
from model.army.rus.artilllery.position_artillery_battery import Position_Artillery_Battery
from model.army.rus.artilllery.position_artillery_half_battery import Position_Artillery_Half_Battery
from model.army.rus.artilllery.unicorn_field_battery import Unicorn_Field_Battery
from model.army.rus.artilllery.unicorn_heavy_battery import Unicorn_Heavy_Battery
from model.army.rus.artilllery.horse_artillery_battery import Horse_Artillery_Battery
from model.army.rus.artilllery.horse_artillery_half_battery import Horse_Artillery_Half_Battery



class AllArtillery(Brigade):

    def __init__(self):
        # список командиров
        self.brigade_commanders_list = []

        # список батальонов (обьектов) включенных в бригаду - по умолчанию unit - тоесть пустышка
        self.brigade_list = []
        self.brigade_list.append(Unit())  # первая легкая рота
        self.brigade_list.append(Unit())  # вторая легкая рота
        self.brigade_list.append(Unit())  # третья легкая рота
        self.brigade_list.append(Unit())  # четвертая легкая рота
        self.brigade_list.append(Unit())  # пятая легкая рота
        self.brigade_list.append(Unit())  # шестая легкая рота
        self.brigade_list.append(Unit())  # первая тяжелая рота
        self.brigade_list.append(Unit())  # вторая тяжелая рота
        self.brigade_list.append(Unit())  # третья тяжелая рота
        self.brigade_list.append(Unit())  # четвертая тяжелая рота
        self.brigade_list.append(Unit())  # первая рота единорогов
        self.brigade_list.append(Unit())  # вторая рота единорогов
        self.brigade_list.append(Unit())  # третья рота единорогов
        self.brigade_list.append(Unit())  # четвертая рота единорогов
        self.brigade_list.append(Unit())  # пятая рота единорогов
        self.brigade_list.append(Unit())  # шестая рота единорогов
        self.brigade_list.append(Unit())  # первая конная рота
        self.brigade_list.append(Unit())  # вторая конная рота
        self.brigade_list.append(Unit())  # третья конная рота

        # возможные вариации для каждого батальона
        self.brigade_list_battalion_list = []
        self.brigade_list_battalion_list.append(self.light_battery_list())  # первая легкая рота - варианты     0
        self.brigade_list_battalion_list.append(self.light_battery_list())  # вторая легкая рота - варианты     1
        self.brigade_list_battalion_list.append(self.light_battery_list())  # третья легкая рота - варианты     2
        self.brigade_list_battalion_list.append(self.light_battery_list())  # четвертая легкая рота - варианты  3
        self.brigade_list_battalion_list.append(self.light_battery_list())  # пятая легкая рота - варианты      4
        self.brigade_list_battalion_list.append(self.light_battery_list())  # шестая легкая рота- варианты      5
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # первая тяжелая рота               6
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # вторая тяжелая рота               7
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # третья тяжелая рота               8
        self.brigade_list_battalion_list.append(self.heavy_battery_list())  # четвертая тяжелая рота            9
        self.brigade_list_battalion_list.append(self.unicorn_battery_list())  # первая рота единорогов          10
        self.brigade_list_battalion_list.append(self.unicorn_battery_list())  # вторая рота единорогов          11
        self.brigade_list_battalion_list.append(self.unicorn_battery_list())  # третья рота единорогов          12
        self.brigade_list_battalion_list.append(self.unicorn_battery_list())  # четвертая рота единорогов       13
        self.brigade_list_battalion_list.append(self.unicorn_battery_list())  # пятая рота единорогов           14
        self.brigade_list_battalion_list.append(self.unicorn_battery_list())  # шестая рота единорогов          15
        self.brigade_list_battalion_list.append(self.horse_battery_list())  # первая конная рота                16
        self.brigade_list_battalion_list.append(self.horse_battery_list())  # вторая конная рота                17
        self.brigade_list_battalion_list.append(self.horse_battery_list())  # третья конная рота                18

        # возможные бонусы для батальонов в бригаде
        self.brigade_bonus_list = []

        # зададим соответствие бонусу - батальона
        self.brigade_bonus_battalion_correspondence = {}

    def light_battery_list(self):
        return [
            Unit(),
            Light_Artillery_Battery(),
            Light_Artillery_Half_Battery()
        ]

    def heavy_battery_list(self):
        return [
            Unit(),
            Position_Artillery_Battery(),
            Position_Artillery_Half_Battery()
        ]

    def unicorn_battery_list(self):
        return [
            Unit(),
            Unicorn_Field_Battery(),
            Unicorn_Heavy_Battery()
        ]

    def horse_battery_list(self):
        return [
            Unit(),
            Horse_Artillery_Battery(),
            Horse_Artillery_Half_Battery()
        ]