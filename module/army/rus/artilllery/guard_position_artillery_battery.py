from module.army.artillery import *
class Guard_Position_Artillery_Battery(Artillery):

    def __init__(self):
        self.type = "Regular Artilery"
        self.armament = "Smoothbore Heavy Artillery"
        self.hand_to_hand = 2
        self.shooting = (4, 2, 2)
        self.morale = 3
        self.stamina = 3
        self.special = {
            "Reliable",
            "Elite 4+",
            "Large"
        }
        self.cost = 52
