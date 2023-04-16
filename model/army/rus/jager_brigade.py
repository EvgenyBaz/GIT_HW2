from model.army.rus.infantry import jager
from model.army.rus.infantry import grenadier


class JagerBrigade:

    def __init__(self):
        self.jager_brigade_list = [

            jager.Jager()
        ]

        self.additional_jager_brigade_list = [
            grenadier.Grenadier()
        ]

    def get_list_of_jager_brigade(self):
        return self.jager_brigade_list

    def get_additional_list_of_jager_brigade(self):
        return self.additional_jager_brigade_list
