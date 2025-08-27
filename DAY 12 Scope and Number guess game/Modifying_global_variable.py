enemies=1
# def increase_enemies():
#     global enemies            #Refering to the global variable enemies (Not recommonded)
#     enemies+=23
#     print(f"Enemies inside the function {enemies}")

# increase_enemies()
# print(f"Enemies outside the function {enemies}")

# Method 2 using return statement
def increase_enemies(enemy):
    print(f"Enemies inside the function {enemies}")
    return enemy+23

enemies=increase_enemies(enemies)
print(f"Enemies outside the function {enemies}")


# Global Constant

'''
You can define global constants in your code file for easy access. 
Their job is meant to be "set and forget" so you can use their values 
but never need to mofy them.

Naming Convention
Global constants are normally declared in ALL_CAPS with a underscore in between.
'''

# Ex
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

