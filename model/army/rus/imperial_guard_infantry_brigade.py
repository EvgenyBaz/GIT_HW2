from model.army.rus.infantry import life_guard_infantry
from model.army.rus.infantry import life_guard_jager
from model.army.rus.artilllery import guard_light_artillery_battery
from model.army.rus.artilllery import guard_light_artillery_half_battery
from model.army.rus.artilllery import guard_position_artillery_battery
from model.army.rus.artilllery import guard_position_artillery_half_battery

class LifeGuardInfantryBrigade:

    def __init__(self):

        self.life_guard_infantry_brigade_list = [
            life_guard_infantry.LifeGuardInfantry(),
            life_guard_jager.LifeGuardJager
        ]

        self.additional_life_infantry_brigade_list = [
            guard_light_artillery_half_battery.Guard_Light_Artillery_Half_Battery(),
            guard_light_artillery_battery.Guard_Light_Artillery_Battery,
            guard_position_artillery_half_battery.Guard_Position_Artillery_Half_Battery(),
            guard_position_artillery_battery.Guard_Position_Artillery_Battery()

        ]


    def get_list_of_life_guard_infantry_brigade(self):
        return self.life_guard_infantry_brigade_list

    def get_additional_list_of_life_guard_infantry_brigade(self):
        return self.additional_life_infantry_brigade_list

