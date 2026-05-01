class InteractionSystem:
    def __init__(self, fn, world):
        self.fn = fn
        self.world = world

    def update(self, entity):
        position = entity.components.get("position")
        state = entity.components.get("state")
        t = entity.components.get("type") #type
        if not position or not state: return

        for other in self.world.entities:
            if other is entity: continue

            otherPosition = other.components.get("position")
            otherType = other.components.get("type")
            otherState = other.components.get("state")
            if not otherPosition: continue

            if abs(position.x - otherPosition.x) <= 1 and abs(position.y - otherPosition.y) <= 1:
                if not otherState.alive: continue

                self.fn(t, state, otherType, otherState)