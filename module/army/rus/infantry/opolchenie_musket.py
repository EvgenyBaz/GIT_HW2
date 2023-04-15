from module.army.infantry import *
class OpolchenieMusket(Infantry):

    def __init__(self):
        self.name = "Opolchenie with Musket"
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 5
        self.shooting = 2
        self.morale = 5
        self.stamina = 3
        self.special = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost = 23
        self.bonus = {}
        self.bonus_cost = 0