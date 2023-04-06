from module.army.artillery import *
class Unicorn_Heavy_Battery(Artillery):

    def __init__(self):
        self.type = "Unicorn Heavy Battery"
        self.type = "Regular Artillery"
        self.armament = "Smoothbore Heavy Howitzer"
        self.hand_to_hand = 1
        self.shooting = (2, 2, 2)
        self.morale = 4
        self.stamina = 2
        self.special = {
            "20 pdr"
        }
        self.cost = 27
