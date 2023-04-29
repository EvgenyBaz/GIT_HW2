from model.army.rus.infantry_brigade import InfantryBrigade
from model.army.rus.jager_brigade import JagerBrigade
from model.army.rus.combined_grenadier_brigade import CombinedGrenadierBrigade
from model.army.rus.grenadier_brigade import GrenadierBrigade
from model.army.rus.light_cavalry_brigade import LightCavalryBrigade
from model.army.rus.heavy_cavalry_brigade import HeavyCavalryBrigade
from model.army.rus.cossack_brigade import CossackBrigade
from model.army.rus.imperial_guard_infantry_brigade import LifeGuardInfantryBrigade
from model.army.rus.imperial_guard_light_cavalry_brigade import LifeGuadLightCavalryBrigade
from model.army.rus.imperial_guard_heavy_cavalry_brigade import LifeGuadHeavyCavalryBrigade
from model.army.rus.all_artillery import AllArtillery




from model.army.rus.commanders.commander_skill7 import CommanderSkill7
from model.army.rus.commanders.commander_skill8 import CommanderSkill8
from model.army.rus.commanders.wurttemberg import Wurttemberg
from model.army.rus.commanders.barclayDeTolly import BarklayDeTolly
from model.army.rus.commanders.denisov import Denisov
from model.army.rus.commanders.bagration import Bagration
from model.army.rus.commanders.kutaisov import Kutaisov
from model.army.rus.commanders.kutuzov import Kutuzov
from model.army.rus.commanders.platov import Platov
from model.army.rus.commanders.stroganov import Stroganov
from model.army.rus.commanders.vorontsov import Vorontsov
from model.army.rus.commanders.bogdanovsky import Bogdanovsky

class RusDivision:

    def __init__(self):
        self.division_list = [
            InfantryBrigade(),              #0
            InfantryBrigade(),              #1
            InfantryBrigade(),              #2
            JagerBrigade(),                 #3
            CombinedGrenadierBrigade(),     #4
            GrenadierBrigade(),             #5
            LightCavalryBrigade(),          #6
            HeavyCavalryBrigade(),          #7
            CossackBrigade(),               #8
            LifeGuardInfantryBrigade(),     #9
            LifeGuadLightCavalryBrigade(),  #10
            LifeGuadHeavyCavalryBrigade(),  #11
            AllArtillery()                  #12
        ]

        self.division_commanders_list = [
            CommanderSkill7(),
            CommanderSkill8(),
            Bagration(),
            Kutuzov(),
            BarklayDeTolly(),
            Wurttemberg(),
            Denisov(),
            Kutaisov(),
            Platov(),
            Stroganov(),
            Vorontsov(),
            Bogdanovsky()
        ]

    def get_list_commanders_names(self):
        division_cmndrs_names = []
        for cmndr in self.division_commanders_list:
            division_cmndrs_names.append(cmndr.get_name_of_commander())
        return division_cmndrs_names

    # по порядковому номеру в списке командиров возвращает его стоимость
    def get_costs_of_commander(self, index):
        return self.division_commanders_list[index].get_cost_of_commander()

    def get_list_of_division(self):
        return self.division_list

    def get_brigade(self, brigade_order):
        return self.division_list[brigade_order]
