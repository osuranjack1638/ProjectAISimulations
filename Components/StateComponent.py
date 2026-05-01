class StateComponent:
    def __init__(self):
        self.alive = True
        self.energy = 100

    def apply(self, entity):
        entity.components["state"] = self