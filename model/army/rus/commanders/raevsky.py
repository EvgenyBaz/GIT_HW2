from model.army.basic_commander import BasicCommander
class Raevsky(BasicCommander):
    def __init__(self):
        self.name = "Lieutenant General  Nikolay Nikolaevitch Raevsky. CS 8"
        self.cost = 100
        self.special = {
            "Combat attack +2 Dice. Inspirational."
        }