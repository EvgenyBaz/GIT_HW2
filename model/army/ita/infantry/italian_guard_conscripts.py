from model.army.infantry import Infantry
class ItalianGuardsConscripts(Infantry):

    name = "Italian Guards Conscripts"
    def __init__(self):
        self.type = "Regular Infantry"
        self.armament = "Smoothbore Musket"
        self.hand_to_hand = 6
        self.shooting = 3
        self.morale = 4
        self.stamina = 3
        self.special = {
            "Pas de charge",
            "Reliable Elite 5+"
        }
        self.cost = 46
        self.bonus = {}
        self.bonus_cost = 0

