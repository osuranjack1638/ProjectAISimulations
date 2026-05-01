class StateSystem:
    def __init__(self, fn):
        self.fn = fn

    def update(self, entity):
        state = entity.components.get("state")
        if not state: return

        self.fn(state, entity)