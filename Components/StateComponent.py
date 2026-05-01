class StateComponent:
    def __init__(self):
        self.alive = True

    def apply(self, entity):
        entity.components["state"] = self