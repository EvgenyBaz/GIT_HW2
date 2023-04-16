from model.army.artillery import *
class Guard_Light_Artillery_Half_Battery(Artillery):

    def __init__(self):
        self.name = "Guard Light Artillery Half Battery"
        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 3
        self.stamina = 2
        self.special = {
            "Reliable",
            "Elite 4+"
        }
        self.cost = 36
