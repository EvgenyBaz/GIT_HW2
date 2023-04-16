from model.army.rus.infantry import combined_grenadier


class CombinedGrenadierBrigade:

    def __init__(self):
        self.combined_grenadier_brigade_list = [

            combined_grenadier.CombinedGrenadier()

        ]

    def get_list_of_combined_grenadier_brigade(self):
        return self.combined_grenadier_brigade_list
