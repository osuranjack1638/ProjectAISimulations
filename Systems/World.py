import random


class World:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self.entities = []
        self.systems = []

    def addEntity(self, entity):
        self.entities.append(entity)

    def removeEntity(self, entity):
        self.entities.remove(entity)

    def addSystem(self, system):
        self.systems.append(system)

    def tick(self):
        for system in self.systems:
            for entity in self.entities:
                system.update(entity)