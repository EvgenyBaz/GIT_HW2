from model.army.basic_commander import BasicCommander
class Stroganov(BasicCommander):
    def __init__(self):
        self.name = "Major General Pavel Stroganov. CS 7 "
        self.cost = 25
        self.special = {
            "Combat attack +1 Dice. Decisive. Irresponsible"
        }