from model.army.basic_commander import BasicCommander
class Wurttemberg(BasicCommander):
    def __init__(self):
        self.name = "Major General Eugene von Wurttemberg. CS 8 "
        self.cost = 100
        self.special = {
            "Headsrtong. Combat attack +2 Dice"
        }