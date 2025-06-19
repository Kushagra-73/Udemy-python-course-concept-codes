# python uses mersenne twister as pseudorandom number genration


import random  #We first need to import any module intpo python ide to use it
#____________________________________________________
# random.randint(a,b) == Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

# random_integer = random.randint(1,10) #starts from 1 and goes upto 10 including 10 and it can get any natural number in [1,10]
# print(random_integer)

#______________________________________________________

# random.random() == Return the next random floating-point number in the range 0.0 <= X < 1.0
# Does not take any input and its range is [0,1)

rand_num_0_to_1=random.random() *10
print(rand_num_0_to_1)



'''
random.uniform(a, b)
Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

The end-point value b may or may not be included in the range depending on floating-point rounding in the expression a + (b-a) * random().
'''

random_float=random.uniform(12,20) #Inclusive of 12 and 20
print(random_float)

#USE random.random() instead of random.uniform

#___________________________________________________________________________________________

#Heads or Tails

ran=random.randint(1,2)
if ran==1:
    print("Heads")
else:
    print("Tails")
