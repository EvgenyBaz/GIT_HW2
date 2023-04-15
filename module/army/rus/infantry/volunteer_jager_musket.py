from module.army.infantry import *


class VolunteerJagerMusket(Infantry):

    def __init__(self):
        self.name = "Volunteer Jager with Musket"
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 4
        self.special = {
            "Militia",
            "Untested",
            "Unreliable",
            "Lacking Initiative"
        }
        self.cost = 37
        self.bonus = {}
        self.bonus_cost = 0
