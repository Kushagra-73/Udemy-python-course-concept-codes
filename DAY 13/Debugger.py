import random
import maths


def mutate(a_list):
    b_list = []
    new_list = 0
    for item in a_list:
        new_list = item * 2
        new_list += random.randint(1, 3)
        new_list = maths.add(new_list, item)
        b_list.append(new_list)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13]) 