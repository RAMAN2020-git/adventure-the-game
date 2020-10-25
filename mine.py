import random

world = []

blocks = {
  1: "Grass",
  2: "Stone",
  3: "Wood"
}


for i in range(10):
    world.append(blocks[random.randint(1,3)])

print("Char")
print(world)
