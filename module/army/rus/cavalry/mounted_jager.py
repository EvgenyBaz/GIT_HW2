from module.army.cavalry import *
class MountedJager(Cavalry):

    def __init__(self):
        self.name = "Mounted Jager"
        self.type = "Regular Cavalry"
        self.armament = "Sabre"
        self.hand_to_hand = 6
        self.shooting = 0
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Marauder"
        }
        self.cost = 41
