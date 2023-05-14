from model.army.artillery import Artillery
class GuardPositionArtilleryBattery(Artillery):
    name = "Guard Position Artillery Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Heavy Artillery"
        self.hand_to_hand = 2
        self.shooting = (4, 2, 2)
        self.morale = 3
        self.stamina = 3
        self.special = {
            "Reliable",
            "Elite 4+",
            "Large"
        }
        self.cost = 52
        self.bonus = {}
        self.bonus_cost = 0
