import random


class WorldContext:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)