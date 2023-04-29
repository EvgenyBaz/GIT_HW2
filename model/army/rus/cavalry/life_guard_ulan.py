from model.army.cavalry import *
class LifeGuardUlan(Cavalry):
    name = "Life Guard Ulan"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Lance"
        self.hand_to_hand = 8
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Reliable",
            "Lancer",
            "Marauder"
        }
        self.cost = 54
        self.bonus = {}
        self.bonus_cost = 0
