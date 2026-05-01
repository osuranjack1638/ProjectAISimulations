class TypeComponent:
    def __init__(self, entityType):
        self.type = entityType

    def apply(self, entity):
        entity.components["type"] = self