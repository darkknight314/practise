import random

# creating a random list
bunti = []
for i in range(10):
    bunti.append(random.randrange(1, 100, 1))
print(bunti)

# printing even elements
soi = []
for bubli in bunti:
    if bubli % 2 == 0:
        soi.append(bubli)
print(soi)
