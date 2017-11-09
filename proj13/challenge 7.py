import random

# creating a random list
random_list = []
for i in range(10):
    random_list.append(random.randrange(1, 100, 1))
print(random_list)

# printing even elements
even_terms = []
for item in random_list:
    if item % 2 == 0:
       even_terms.append(item)
print(even_terms)
