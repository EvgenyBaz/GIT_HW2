from model.army.basic_commander import BasicCommander
class Bagration(BasicCommander):
    def __init__(self):
        self.name = "General of Infantry Pyotr Ivanovich Bargation. CS 9 "
        self.cost = 175
        self.special = {
            "Combat attack +2 Dice. Decisive. Inspirational. 'Lion of the army': \
Once per game a Russian unit of cavalry or infantry can re-roll a Break test results as if is were Valiant"
        }