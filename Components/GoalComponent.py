class GoalComponent:
    def __init__(self):
        self.target = None
        self.state = "idle"

    def addTarget(self, target): # target = function
        self.target = target

    def removeTarget(self, target):
        self.target = None

    def apply(self, entity):
        entity.components["goal"] = self