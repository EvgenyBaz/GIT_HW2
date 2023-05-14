from model.army.infantry import Infantry
class RoyalGuardGrenadier(Infantry):

    name = "Royal Guard Grenadier"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 7
        self.shooting = 3
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Pas de charge",
            "Reliable Elite 4+"
        }
        self.cost = 49
        self.bonus = {}
        self.bonus_cost = 0

