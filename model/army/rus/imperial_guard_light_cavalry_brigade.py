from model.army.rus.cavalry.life_guard_cossack import LifeGuardCossack
from model.army.rus.cavalry.life_guard_ulan import LifeGuardUlan
from model.army.rus.cavalry.life_guard_hussars import LifeGuardHussars
from model.army.rus.cavalry.life_guard_dragoon import LifeGuardDragoon
from model.army.rus.artilllery.guard_horse_artillery_battery import GuardHorseArtilleryBattery
from model.army.rus.artilllery.guard_horse_artillery_half_battery import GuardHorseArtilleryHalfBattery

class LifeGuadLightCavalryBrigade:

    def __init__(self):
        self.life_guard_light_cavalry_brigade_list = [

            LifeGuardCossack(),
            LifeGuardUlan(),
            LifeGuardHussars(),
            LifeGuardDragoon()

        ]

        self.additional_life_guard_light_cavalry_brigade_list = [
            GuardHorseArtilleryHalfBattery(),
            GuardHorseArtilleryBattery()

        ]

    def get_list_of_life_guard_light_cavalry_brigade(self):
        return self.life_guard_light_cavalry_brigade_list

    def get_additional_list_of_life_guard_light_cavalry_brigade(self):
        return self.additional_life_guard_light_cavalry_brigade_list

