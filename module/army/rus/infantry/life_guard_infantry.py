from module.army.infantry import *
class LifeGuardInfantry(Infantry):

    def __init__(self):
        self.type = "Regular Indantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 7
        self.shooting = 3
        self.morale = 3
        self.stamina = 4
        self.special = {
            "Tough Fighter",
            "Poor",
            "Skirmisher",
            "Reliable"
            "Elite 3+"
            "Valiant"
        }
        self.cost = 61
