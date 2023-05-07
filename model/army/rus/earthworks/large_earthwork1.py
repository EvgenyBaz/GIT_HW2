from model.army.unit import *
class LargeEarthWork1(Unit):
    name = "Large EarthWork save +1"
    def __init__(self):

        self.type = "EarthWork"
        self.armament = "none"
        self.hand_to_hand = 0
        self.shooting = 0
        self.morale = 0
        self.stamina = 0
        self.special = {"save +1"}
        self.cost = 25
        self.bonus = {}
        self.bonus_cost = 0