from module.army.cavalry import *
class Dragoon(Cavalry):

    def __init__(self):
        self.name = "Dragoon"
        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 8
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Heavy Cavalry D1"
        }
        self.cost = 44
