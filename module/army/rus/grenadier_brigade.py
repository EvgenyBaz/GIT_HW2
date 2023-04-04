from module.army.rus.infantry import grenadier


class GrenadierBrigade:

    def __init__(self):
        self.grenadier_brigade_list = [

            grenadier.Grenadier()

        ]

    def get_list_of_grenadier_brigade(self):
        return self.grenadier_brigade_list
