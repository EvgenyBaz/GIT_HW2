from module.army.artillery import *
class Position_Artillery_Half_Battery(Artillery):

    def __init__(self):
        self.name = "Position Artillery Half Battery"
        self.type = "Regular Artillery"
        self.armament = "Smoothbore Heavy Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 4
        self.stamina = 2
        self.special = {

        }
        self.cost = 28
