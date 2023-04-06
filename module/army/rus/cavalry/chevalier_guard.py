from module.army.cavalry import *
class ChevalierGuard(Cavalry):

    def __init__(self):
        self.name = "Chevalier Guard"
        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 10
        self.shooting = 0
        self.morale = 3
        self.stamina = 3
        self.special = {
            "Reliable",
            "Heavy Cavalry D3"
        }
        self.cost = 60
