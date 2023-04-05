from module.army.infantry import *
class Grenadier(Infantry):

    def __init__(self):
        self.type = "Regular Indantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 7
        self.shooting = 3
        self.morale = 4
        self.stamina = 4
        self.special = {
            "Tough Fighter",
            "Poor",
            "Skirmisher",
            "Lacking Initiative"
            "Elite 4+"
        }
        self.cost = 48