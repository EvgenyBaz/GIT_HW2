from model.army.cavalry import *
class LifeGuardDragoon(Cavalry):
    name = "Life Guard Dragoon"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 9
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Reliable",
            "Heavy Cavalry D1"
        }
        self.cost = 54
        self.bonus = {}
        self.bonus_cost = 0
