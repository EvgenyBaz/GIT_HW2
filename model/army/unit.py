class Unit:
    name = "empty"
    presence = 0

    def __init__(self):
        # self.name = "empty"
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
        self.bonus = {}
        self.bonus_cost = 0

    def get_cost_of_battalion(self):
        return self.cost

    def get_bonus_of_battalion(self):
        result = "  "
        for bonus in self.bonus:
            result = result + bonus + ", "
        return result[0:-2]


    @classmethod
    def get_name_of_battalion(cls):
        return cls.name






