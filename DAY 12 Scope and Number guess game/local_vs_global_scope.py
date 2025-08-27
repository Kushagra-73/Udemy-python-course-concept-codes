# enemies=1


# def increase_enimies():
#     enemies=2
#     print(f"enimies inside the funtion {enemies}")

# increase_enimies()

# print(f"enemies outside the function {enemies}")




# Local Scope (exist within a funcitons)
# def drink_potion():
#     potion_strength=2        #When you create a new variable or new function inside the 
#     print(potion_strength)   #fucntion it is only accessible when you are inside that function
#                              #due to local scope

# drink_potion()
# print(potion_strength)    #NameError: name 'potion_strength' is not defined (due to local scope)

# Global Scope - applies to any namespaces be it variable, funcition
player_health=10     #Global Variable  - available within or outside function anywhere

# def drink_potion():
#     potion_strength=2     #Local Variable
#     # print(potion_strength)
#     print(player_health)

# drink_potion()
# print(player_health)

'''
Local Scope
Variables (or functions) declared inside functions have local 
scope (also called function scope). They are only seen by other 
code within the same block of code.
'''

'''
Global Scope
Variables or functions declared at the top level (unindented) 
of a code file have global scope. It is accessible anywhere in the code file.
'''