from model.army.basic_commander import BasicCommander
class CommanderSkill8(BasicCommander):
    presence = 1
    def __init__(self):
        self.name = "command stаff 8"
        self.cost = 20
        self.special = {
            "+1 to command"
        }