# Built in modules (random.py)

from random import choice, random, randint, shuffle

# get random number between 0-1
print(random())

# get random integer between given range
print(randint(1, 10))

# get choice from given choices list
print(choice([1, 2, 3, 4, 5]))

# randmoly shuffle the given list
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)
