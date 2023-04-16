from model.army.artillery import *
class Unicorn_Field_Battery(Artillery):

    def __init__(self):
        self.type = "Unicorn Field Battery"
        self.type = "Regular Artilery"
        self.armament = "Smoothbore Field Howizer"
        self.hand_to_hand = 1
        self.shooting = (2, 2, 2)
        self.morale = 4
        self.stamina = 2
        self.special = {
            "10 pdr"
        }
        self.cost = 23
