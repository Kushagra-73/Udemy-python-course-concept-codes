# There is no block scope in Python
# If you were to create a new variable inside if block,or while or for loop this does not
# count as a fence i.e.it has the same scope as its enclosing function or if there's no
# enclosing function, then it gas global scope.

game_level=3
enemies=["Skeleton","Zombie","Alien"]

# if game_level<5:                
#     new_enemy=enemies[0]

# print(new_enemy)

# But if it is supposed to be inside a function then it will have a local scope for new_enemy variable
# def create_enemy():
#     if game_level<5:                
#         new_enemy=enemies[0]

# print(new_enemy)    #NameError: name 'new_enemy' is not defined