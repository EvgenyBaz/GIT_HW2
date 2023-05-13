from model.army.basic_commander import BasicCommander
class Denisov(BasicCommander):
    def __init__(self):
        self.name = "Major General Vasili Denisov. CS 8 "
        self.cost = 100
        self.special = {
            "Combat attack +1 Dice. Cossack cavalry under his command can charge normally"
        }