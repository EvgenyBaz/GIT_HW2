from module.army.artillery import *
class Guard_Horse_Artillery_Battery(Artillery):

    def __init__(self):
        self.type = "Regular Artilery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 2
        self.shooting = (4, 2, 2)
        self.morale = 3
        self.stamina = 2
        self.special = {
            "Marauder",
            "Reliable",
            "Elite 4+",
            'Large'
        }
        self.cost = 27
