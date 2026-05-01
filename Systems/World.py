import random


class World:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self.entities = []
        self.systems = []
        self.map = []

    def createMap(self, width=10, height=10):
        for r in range(width):
            row = []
            for c in range(height):
                row.append(None)
            self.map.append(row)

    def printMap(self):
        for row in self.map:
            print(row)

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