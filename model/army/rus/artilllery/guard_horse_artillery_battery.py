from model.army.artillery import *
class GuardHorseArtilleryBattery(Artillery):
    name = "Guard Horse Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 2
        self.shooting = (4, 2, 2)
        self.morale = 3
        self.stamina = 2
        self.special = {
            "Marauder",
            "Reliable",
            "Elite 4+",
            'Large'
        }
        self.cost = 27
        self.bonus = {}
        self.bonus_cost = 0
