class TypeSystem:
    def __init__(self, fn):
        self.fn = fn

    def update(self, entity):
        t = entity.components.get("type")
        state = entity.components.get("state")
        if not t or not state: return

        self.fn(t, state)