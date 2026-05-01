from Components.StateComponent import StateComponent
from Components.TypeComponent import TypeComponent
from Entity.Entity import Entity
from Systems.TypeSystem import TypeSystem
from Systems.World import World

world = World()
wState = StateComponent({"Supply": 0, "Demand": 0})

def createEntity(components):
    e = Entity()
    for component in components:
        component.apply(e)
    world.addEntity(e)
    return e

for i in range(5):
    createEntity([TypeComponent("Supplier"), StateComponent({"AmountCreated": 2})])

for i in range(5):
    createEntity([TypeComponent("Demander"), StateComponent({"AmountBought": 2})])


def typeFn(t, s): #t = type, s = state
    if t.type == "Supplier":
        wState.data["Supply"] += s.data["AmountCreated"]
    elif t.type == "Demander":
        wState.data["Demand"] += s.data["AmountBought"]

world.addSystem(TypeSystem(typeFn))

for tick in range(10):
    print(f"\nTick {tick+1}")
    wState.data["Supply"] = 0
    wState.data["Demand"] = 0
    world.tick()
    wState.data["Supply"] -= wState.data["Demand"]

    print(wState.data)