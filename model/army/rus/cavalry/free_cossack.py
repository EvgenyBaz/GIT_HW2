from model.army.cavalry import *
class FreeCossack(Cavalry):
    name = "Free Cossack regiment"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Lance or Bow"
        self.hand_to_hand = 5
        self.shooting = 2
        self.morale = 5
        self.stamina = 3
        self.special = {
            "Lancer",
            "Marauder",
            "Unreliable"
        }
        self.cost = 0
        self.bonus = {}
        self.bonus_cost = 0
