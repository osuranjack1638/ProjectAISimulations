class DecisionSystem:
    def __init__(self, fn):
        self.fn = fn

    def update(self, entity):
        state = entity.components.get("state")
        goal = entity.components.get("goal")
        if not state or not goal: return

        self.fn(state, goal)