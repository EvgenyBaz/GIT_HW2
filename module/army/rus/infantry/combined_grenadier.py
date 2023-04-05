from module.army.infantry import *
class CombinedGrenadier(Infantry):

    def __init__(self):
        self.type = "Regular Indantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 4
        self.special = {
            "Tough Fighter",
            "Poor",
            "Skirmisher",
            "Lacking Initiative"
        }
        self.cost = 41