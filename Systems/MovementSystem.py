class MovementSystem:
    def __init__(self, fn):
        self.fn = fn

    def update(self, entity):
        position = entity.components.get("position")
        movement = entity.components.get("movement")
        if not position or not movement: return

        self.fn(position, movement)