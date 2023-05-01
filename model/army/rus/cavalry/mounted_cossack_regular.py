from model.army.cavalry import *
class MountedCossackRegular(Cavalry):
    name = "Mounted Cossack"
    presence = 1
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Lance"
        self.hand_to_hand = 5
        self.shooting = 0
        self.morale = 5
        self.stamina = 3
        self.special = {
            "Lancer",
            "Marauder",
            "Unreliable"
        }
        self.cost = 39
        self.bonus = {}
        self.bonus_cost = 0
