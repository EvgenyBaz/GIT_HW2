from model.army.basic_commander import BasicCommander
class Vorontsov(BasicCommander):
    def __init__(self):
        self.name = "Major General Mikhail Vorontsov. CS 8 "
        self.cost = 75
        self.special = {
            "Combat attack +1 Dice. Decisive."
        }