from model.army.basic_commander import BasicCommander
class Kutaisov(BasicCommander):
    def __init__(self):
        self.name = "Major General Aleksander Ivanovich Kutaisov. CS 7 "
        self.cost = 150
        self.special = {
            "Combat attack +1 Dice. Decisive. Headstrong. Aggressive. Russian batteries ignore their proximity rule."
        }