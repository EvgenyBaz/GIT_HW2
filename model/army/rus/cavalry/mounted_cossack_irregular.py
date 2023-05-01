from model.army.cavalry import *
class MountedCossackIrregular(Cavalry):
    name = "Irregular Mounted Cossack"
    presence = 1
    def __init__(self):

        self.type = "Irregular Cavalry"
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
        self.cost = 37
        self.bonus = {}
        self.bonus_cost = 0
