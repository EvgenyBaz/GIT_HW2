from model.army.earthworks import *
class StandardEarthWork(EarthWorks):
    name = "Standard EarthWork"
    def __init__(self):

        self.type = "EarthWork"
        self.armament = "none"
        self.hand_to_hand = 0
        self.shooting = 0
        self.morale = 0
        self.stamina = 0
        self.special = {}
        self.cost = 15
        self.bonus = {}
        self.bonus_cost = 0