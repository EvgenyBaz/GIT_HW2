from module.army.rus.cavalry import dragoon
from module.army.rus.cavalry import hussars
from module.army.rus.cavalry import ulan
from module.army.rus.cavalry import mounted_cossack_regular
from module.army.rus.cavalry import mounted_cossack_irregular


class LightCavalryBrigade:

    def __init__(self):
        self.light_cavalry_brigade_list = [

            dragoon.Dragoon(),
            hussars.Hussars(),
            ulan.Ulan(),
            mounted_cossack_regular.MountedCossackRegular(),
            mounted_cossack_irregular.MountedCossackIrregular()

        ]

    def get_list_of_light_cavalry_brigade(self):
        return self.light_cavalry_brigade_list


