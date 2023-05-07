from model.army.artillery import *
class LightArtilleryBattery(Artillery):
    name = "Light Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Artillery"
        self.hand_to_hand = 2
        self.shooting = (4, 2, 2)
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Large"
        }
        self.cost = 36
        self.bonus = {}
        self.bonus_cost = 0