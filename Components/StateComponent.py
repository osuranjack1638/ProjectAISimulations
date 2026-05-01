class StateComponent:
    def __init__(self, data):
        self.data = data

    def apply(self, entity):
        entity.components["state"] = self