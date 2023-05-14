from model.army.earthworks import EarthWorks
class LargeEarthWork2(EarthWorks):
    name = "Large EarthWork save +2"
    def __init__(self):

        self.type = "EarthWork"
        self.armament = "none"
        self.hand_to_hand = 0
        self.shooting = 0
        self.morale = 0
        self.stamina = 0
        self.special = {"save +2"}
        self.cost = 35
        self.bonus = {}
        self.bonus_cost = 0