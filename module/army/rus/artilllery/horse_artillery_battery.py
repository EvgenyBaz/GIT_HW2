from module.army.artillery import *
class Horse_Artillery_Battery(Artillery):

    def __init__(self):
        self.type = "Regular Artilery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 2
        self.shooting = (4, 2, 2)
        self.morale = 4
        self.stamina = 2
        self.special = {
            "Marauder",
            "Large"
        }
        self.cost = 39
