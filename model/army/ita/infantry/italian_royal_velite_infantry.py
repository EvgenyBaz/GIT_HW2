from model.army.infantry import Infantry
class ItalianRoyalVeliteInfantry(Infantry):

    name = "Italian Royal Velite Infantry"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 7
        self.shooting = 3
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Pas de charge",
            "Reliable Elite 5+"
        }
        self.cost = 47
        self.bonus = {}
        self.bonus_cost = 0

