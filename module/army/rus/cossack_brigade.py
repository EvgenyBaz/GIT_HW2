from module.army.rus.cavalry import mounted_cossack_regular
from module.army.rus.cavalry import mounted_cossack_irregular


class CossackBrigade:

    def __init__(self):
        self.cossack_brigade_list = [

            mounted_cossack_regular.MountedCossackRegular(),
            mounted_cossack_irregular.MountedCossackIrregular()

        ]

    def get_list_of_cossack_brigade(self):
        return self.cossack_brigade_list


