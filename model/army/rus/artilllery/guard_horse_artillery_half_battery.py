from model.army.artillery import *
class GuardHorseArtilleryHalfBattery(Artillery):
    name = "Guard Horse Artillery Half Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 3
        self.stamina = 1
        self.special = {
            "Marauder",
            "Reliable",
            "Elite 4+"
        }
        self.cost = 39
        self.bonus = {}
        self.bonus_cost = 0
