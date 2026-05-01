class MovementSystem:
    def __init__(self, fn):
        self.fn = fn

    def update(self, entity):
        position = entity.components.get("position")
        movement = entity.components.get("movement")
        state = entity.components.get("state")
        if not position or not movement: return
        if state and not state.alive: return

        self.fn(position, movement)