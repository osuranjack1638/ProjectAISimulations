class NameComponent:
    def __init__(self, world):
        self.world = world
        self.generated = set()

        self.prefixes = ["Al", "Ar", "Bel", "Cal", "Dar", "El", "Fen", "Gal", "Hal", "Ian", "Jar", "Kal", "Lor", "Mar", "Nor", "Or", "Per", "Quin", "Rin", "Sar", "Tal", "Ul", "Val", "Wen", "Xan", "Yor", "Zan"]
        self.middles = ["a", "ae", "ai", "an", "ar", "as", "el", "en", "er", "es", "ia", "io", "ir", "is", "or", "on", "ol", "un", "ul", "ur", "var", "mir", "tor", "len", "ven", "dra", "sha", "tha", "kel", "rin"]
        self.suffixes = ["a", "an", "ar", "as", "el", "en", "er", "es", "ia", "ian", "iel", "ion", "ir", "is", "or", "on", "us", "yx", "yx", "ael", "dor", "mir", "th", "dan", "lyn", "ric", "wen", "zor"]


    def generateName(self):
        name = self.world.rng.choice(self.prefixes) + self.world.rng.choice(self.middles) + self.world.rng.choice(self.suffixes)
        while name in self.generated:
            name += str(self.world.rng.randint(0, 9))

        self.generated.add(name)
        return name

    def apply(self, entity):
        entity.components["name"] = self.generateName()