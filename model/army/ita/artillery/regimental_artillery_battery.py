from model.army.artillery import Artillery
class RegimentalArtilleryBattery(Artillery):
    name = "Regimental Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Battalion Artillery"
        self.hand_to_hand = 1
        self.shooting = (1, 1, 1)
        self.morale = 4
        self.stamina = 1
        self.special = {
        }
        self.cost = 11
        self.bonus = {}
        self.bonus_cost = 0