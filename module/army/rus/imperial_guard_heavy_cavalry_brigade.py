from module.army.rus.cavalry import life_guard_cuirassier
from module.army.rus.cavalry import chevalier_guard
from module.army.rus.cavalry import life_guard_horse
from module.army.rus.artilllery import guard_horse_artillery_battery
from module.army.rus.artilllery import guard_horse_artillery_half_battery

class LifeGuadHeavyCavalryBrigade:

    def __init__(self):
        self.life_guard_heavy_cavalry_brigade_list = [

            life_guard_cuirassier.LifeGuardCuirassier(),
            chevalier_guard.ChevalierGuard(),
            life_guard_horse.LifeGuardHorse()

        ]

        self.additional_life_guard_heavy_cavalry_brigade_list = [
            guard_horse_artillery_half_battery.Guard_Horse_Artillery_Half_Battery(),
            guard_horse_artillery_battery.Guard_Horse_Artillery_Battery

        ]

    def get_list_of_life_guard_heavy_cavalry_brigade(self):
        return self.life_guard_heavy_cavalry_brigade_list

    def get_additional_list_of_life_guard_heavy_cavalry_brigade(self):
        return self.additional_life_guard_heavy_cavalry_brigade_list

