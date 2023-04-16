class BasicCommander:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.special = {}

    def get_cost_of_commander(self):
        return self.cost

    def get_name_of_commander(self):
        return self.name
