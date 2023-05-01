from model.army.cavalry import *
class Ulan(Cavalry):
    name = "Ulan"
    presence = 1
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Lance"
        self.hand_to_hand = 7
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Lancer",
            "Marauder"
        }
        self.cost = 48
        self.bonus = {}
        self.bonus_cost = 0
