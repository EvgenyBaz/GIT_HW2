from model.army.artillery import Artillery
class UnicornFieldBattery(Artillery):

    name = "Unicorn Field Battery"
    def __init__(self):

        self.type = "Regular Artilery"
        self.armament = "Smoothbore Field Howizer"
        self.hand_to_hand = 1
        self.shooting = (2, 2, 2)
        self.morale = 4
        self.stamina = 2
        self.special = {
            "10 pdr"
        }
        self.cost = 23
        self.bonus = {}
        self.bonus_cost = 0