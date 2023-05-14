from model.army.artillery import Artillery
class UnicornHeavyBattery(Artillery):

    name = "Unicorn Heavy Battery"
    def __init__(self):

        self.type = "Regular Artillery"
        self.armament = "Smoothbore Heavy Howitzer"
        self.hand_to_hand = 1
        self.shooting = (2, 2, 2)
        self.morale = 4
        self.stamina = 2
        self.special = {
            "20 pdr"
        }
        self.cost = 27
        self.bonus = {}
        self.bonus_cost = 0
