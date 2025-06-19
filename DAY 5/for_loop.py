
# fruits=["apple","bannana","mango"]
# for fruit in fruits:
#     print(fruit)                        #Here first loop gets first value apple as fruit from fruits then again goes to the second value now
#     print(fruit+"pie")


# associating range function with for loop
# for i in range(1,101):
#     print(i)

# sum=0
# for i in range(1,101):      #"range(start,stop,step)"
#     sum+=i

# print(f"The sum is {sum}")


#Fizz BUzz == Note - take conditional statement of intersection always first 

for i in range(1,101):
    
    # print(i)
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    
    else:
        print(i)
         
