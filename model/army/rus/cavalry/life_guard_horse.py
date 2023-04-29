from model.army.cavalry import *
class LifeGuardHorse(Cavalry):
    name = "Life Guard Horse"
    def __init__(self):

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
        self.bonus = {}
        self.bonus_cost = 0
