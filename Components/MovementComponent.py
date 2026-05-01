class MovementComponent:
    def __init__(self, speed=1):
        self.speed = speed

    def apply(self, entity):
        entity.components["movement"] = self