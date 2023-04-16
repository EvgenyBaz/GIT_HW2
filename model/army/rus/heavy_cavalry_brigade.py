from model.army.rus.cavalry import dragoon
from model.army.rus.cavalry import cuirassier


class HeavyCavalryBrigade:

    def __init__(self):
        self.heavy_cavalry_brigade_list = [

            dragoon.Dragoon(),
            cuirassier.Cuirassier()

        ]

    def get_list_of_heavy_cavalry_brigade(self):
        return self.heavy_cavalry_brigade_list


