from module.army.rus.infantry_brigade import InfantryBrigade
from module.army.rus.jager_brigade import JagerBrigade
from module.army.rus.combined_grenadier_brigade import CombinedGrenadierBrigade
from module.army.rus.grenadier_brigade import GrenadierBrigade
from module.army.rus.light_cavalry_brigade import LightCavalryBrigade
from module.army.rus.heavy_cavalry_brigade import HeavyCavalryBrigade
from module.army.rus.cossack_brigade import CossackBrigade
from module.army.rus.imperial_guard_infantry_brigade import LifeGuardInfantryBrigade
from module.army.rus.imperial_guard_light_cavalry_brigade import LifeGuadLightCavalryBrigade
from module.army.rus.imperial_guard_heavy_cavalry_brigade import LifeGuadHeavyCavalryBrigade

class Corps:

    def __init__(self):
        self.corps_list = [
            InfantryBrigade(),
            InfantryBrigade(),
            InfantryBrigade(),
            JagerBrigade(),
            CombinedGrenadierBrigade(),
            GrenadierBrigade(),
            LightCavalryBrigade(),
            HeavyCavalryBrigade(),
            CossackBrigade(),
            LifeGuardInfantryBrigade(),
            LifeGuadLightCavalryBrigade(),
            LifeGuadHeavyCavalryBrigade()

        ]

    def get_list_of_corps(self):
        return self.corps_list
