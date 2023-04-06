from module.army.infantry import *
class VolunteerJagerRifle(Infantry):

    def __init__(self):
        self.name = "Volunteer Jager with Rifle"
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
        self.cost = 40