from model.army.cavalry import Cavalry
class LifeGuardHussars(Cavalry):
    name = "Life Guard Hussars"
    def __init__(self):

        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 7
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Reliable",
            "Marauder"
        }
        self.cost = 47
        self.bonus = {}
        self.bonus_cost = 0
