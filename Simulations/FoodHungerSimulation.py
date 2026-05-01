from Components.MovementComponent import MovementComponent
from Components.NameComponent import NameComponent
from Components.PositionComponent import PositionComponent
from Components.StateComponent import StateComponent
from Components.TypeComponent import TypeComponent
from Entity.Entity import Entity
from Systems.InteractionSystem import InteractionSystem
from Systems.MovementSystem import MovementSystem
from Systems.StateSystem import StateSystem
from Systems.TypeSystem import TypeSystem
from Systems.World import World

world = World()

def createEntity(nComp, pComp, sComp, mComp, tComp):
    entity = Entity()

    nComp.apply(entity)
    pComp.apply(entity)
    sComp.apply(entity)
    mComp.apply(entity)
    tComp.apply(entity)

    world.addEntity(entity)

    return entity


def stateFn(s): #s = state
    if s.energy <= 0:
        s.alive = False

def movementFn(p, m): #p = pos, m = movement/speed
    p.x += world.rng.randint(-1, 1) * m.speed
    p.y += world.rng.randint(-1, 1) * m.speed

def typeFn(t, s): #t = type, s = state
    if t.type == "human":
        s.energy -= 1

def interactionFn(s, oT, oS): #s = state, oT = other type, oS = other state
    if oT == "food":
        s.energy += 5

world.addSystem(TypeSystem(typeFn))
world.addSystem(MovementSystem(movementFn))
world.addSystem(StateSystem(stateFn))
world.addSystem(InteractionSystem(interactionFn, world))

# spawning food
for i in range(3):
    food = Entity()

    food.components["position"] = PositionComponent(world.rng.randint(0, 5), world.rng.randint(0, 5))
    food.components["type"] = TypeComponent("food")
    food.components["state"] = StateComponent()

    world.addEntity(food)

# spawning humans
for i in range(10):
    createEntity(NameComponent(world), PositionComponent(0, 0), StateComponent(), MovementComponent(), TypeComponent("human"))

for tick in range(10):
    print(f"\nTick {tick+1}")
    world.tick()

    for e in world.entities:
        t = e.components["type"].type
        pos = e.components["position"]

        if t == "human":
            state = e.components["state"]
            name = e.components["name"]

            print(name, pos.x, state.energy, state.alive, t)
        elif t == "food":
            print(pos.x, t)