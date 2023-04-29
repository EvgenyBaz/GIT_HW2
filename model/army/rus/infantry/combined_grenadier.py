from model.army.infantry import *
class CombinedGrenadier(Infantry):
    name = "Combined Grenadier"
    presence = 1
    def __init__(self):
        # self.name = "Combined Grenadier"
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 4
        self.special = {
            "Tough Fighter",
            "Poor",
            "Skirmisher",
            "Lacking Initiative"
        }
        self.cost = 41
        self.bonus = {}
        self.bonus_cost = 0