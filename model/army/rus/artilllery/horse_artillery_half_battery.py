from model.army.artillery import *
class Guard_Horse_Artillery_Half_Battery(Artillery):

    def __init__(self):
        self.name = "Guard Horse Artillery Half Battery"
        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 4
        self.stamina = 1
        self.special = {
            "Marauder",
            "Reliable",
            "Elite 4+"
        }
        self.cost = 39
