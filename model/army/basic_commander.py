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

    def get_skills_of_commander(self):
        skills = "  "
        for k in self.special:
            skills = skills + str(k)+", "
        return skills[0:-2]

