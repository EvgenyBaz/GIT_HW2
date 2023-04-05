class Unit:

    def __init__(self):
        self.name = "empty"
        self.type = "unit"
        self.armament = "weapon"
        self.hand_to_hand = 4
        self.shooting = 4
        self.morale = 4
        self.stamina = 4
        self.special = {
            "property"
        }
        self.cost = 0

    def get_cost_of_battalion(self):
        return self.cost
