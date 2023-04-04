from module.army.rus.cavalry import life_guard_cossack
from module.army.rus.cavalry import life_guard_ulan
from module.army.rus.cavalry import life_guard_hussars
from module.army.rus.cavalry import life_guard_dragoon
from module.army.rus.artilllery import guard_horse_artillery_battery
from module.army.rus.artilllery import guard_horse_artillery_half_battery

class LifeGuadLightCavalryBrigade:

    def __init__(self):
        self.life_guard_light_cavalry_brigade_list = [

            life_guard_cossack.LifeGuardCossack(),
            life_guard_ulan.LifeGuardUlan(),
            life_guard_hussars.LifeGuardHussars(),
            life_guard_dragoon.LifeGuardDragoon()

        ]

        self.additional_life_guard_light_cavalry_brigade_list = [
            guard_horse_artillery_half_battery.Guard_Horse_Artillery_Half_Battery(),
            guard_horse_artillery_battery.Guard_Horse_Artillery_Battery

        ]

    def get_list_of_life_guard_light_cavalry_brigade(self):
        return self.life_guard_light_cavalry_brigade_list

    def get_additional_list_of_life_guard_light_cavalry_brigade(self):
        return self.additional_life_guard_light_cavalry_brigade_list

