from model.army.artillery import Artillery
class PositionArtilleryHalfBattery(Artillery):
    name = "Position Artillery Half Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Heavy Artillery"
        self.hand_to_hand = 1
        self.shooting = (3, 1, 1)
        self.morale = 4
        self.stamina = 2
        self.special = {

        }
        self.cost = 28
        self.bonus = {}
        self.bonus_cost = 0
