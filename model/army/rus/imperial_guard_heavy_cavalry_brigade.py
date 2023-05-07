from model.army.rus.cavalry.life_guard_cuirassier import LifeGuardCuirassier
from model.army.rus.cavalry.chevalier_guard import ChevalierGuard
from model.army.rus.cavalry.life_guard_horse import LifeGuardHorse
from model.army.rus.artilllery.guard_horse_artillery_battery import GuardHorseArtilleryBattery
from model.army.rus.artilllery.guard_horse_artillery_half_battery import GuardHorseArtilleryHalfBattery

class LifeGuadHeavyCavalryBrigade:

    def __init__(self):
        self.life_guard_heavy_cavalry_brigade_list = [

            LifeGuardCuirassier(),
            ChevalierGuard(),
            LifeGuardHorse()

        ]

        self.additional_life_guard_heavy_cavalry_brigade_list = [
            GuardHorseArtilleryHalfBattery(),
            GuardHorseArtilleryBattery()
        ]

    def get_list_of_life_guard_heavy_cavalry_brigade(self):
        return self.life_guard_heavy_cavalry_brigade_list

    def get_additional_list_of_life_guard_heavy_cavalry_brigade(self):
        return self.additional_life_guard_heavy_cavalry_brigade_list

