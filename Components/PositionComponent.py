class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clamp(self, maxX, maxY):
        self.x = max(0, min(self.x, maxX))
        self.y = max(0, min(self.y, maxY))

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def apply(self, entity):
        entity.components["position"] = self