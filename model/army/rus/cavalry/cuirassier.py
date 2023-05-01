from model.army.cavalry import *
class Cuirassier(Cavalry):
    name = "Cuirassier"
    presence = 1
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 9
        self.shooting = 0
        self.morale = 3
        self.stamina = 3
        self.special = {
            "Reliable",
            "Heavy Cavalry D3"
        }
        self.cost = 58
        self.bonus = {}
        self.bonus_cost = 0
