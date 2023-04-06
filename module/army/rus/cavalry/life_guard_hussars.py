from module.army.cavalry import *
class LifeGuardHussars(Cavalry):

    def __init__(self):
        self.name = "Life Guard Hussars"
        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 7
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Reliable",
            "Marauder"
        }
        self.cost = 47
