import random


class World:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self.entities = []
        self.systems = []

    def tick(self):
        for system in self.systems:
            for entity in self.entities:
                system.update(entity)