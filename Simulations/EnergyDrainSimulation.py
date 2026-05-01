from Components.MovementComponent import MovementComponent
from Components.NameComponent import NameComponent
from Components.PositionComponent import PositionComponent
from Components.StateComponent import StateComponent
from Components.TypeComponent import TypeComponent
from Entity.Entity import Entity
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


def typeFn(t, s): #t = type, s = state
    if t.type == "human":
        s.energy -= 1

def movementFn(p, m): #p = pos, m = movement/speed
    p.x += world.rng.randint(-1, 1) * m.speed
    p.y += world.rng.randint(-1, 1) * m.speed

def stateFn(s): #s = state
    s.energy -= 1
    if s.energy <= 0:
        s.alive = False


world.addSystem(TypeSystem(typeFn))
world.addSystem(MovementSystem(movementFn))
world.addSystem(StateSystem(stateFn))

for i in range(5):
    e = createEntity(
        nComp=NameComponent(world),
        pComp=PositionComponent(0, 0),
        sComp=StateComponent(),
        mComp=MovementComponent(1),
        tComp=TypeComponent("human")
    )

    world.addEntity(e)

for tick in range(10):
    print(f"\nTick {tick}")
    world.tick()

    for e in world.entities:
        pos = e.components["position"]
        state = e.components["state"]
        name = e.components["name"]

        print(name, pos.x, state.energy, state.alive)