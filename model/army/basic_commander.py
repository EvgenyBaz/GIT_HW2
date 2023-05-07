class BasicCommander:
    presence = 0
    def __init__(self):
        self.name = "empty"
        self.cost = 0
        self.special = {}

    def get_cost_of_commander(self):
        return self.cost

    def get_name_of_commander(self):
        return self.name
