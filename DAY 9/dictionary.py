"""
A dictionary in Python functions similarly to a dictionary in real life. It's a data 
structure that allows us to associate a key to a value and pair the two pieces of data 
together.
"""

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

# ACCESSING A KEY VALUE PAIR
print(programming_dictionary["Function"])

# ADDING ELEMENT IN THE DICTIONARY
programming_dictionary["Loop"]="An error in a program that prevents the program from running as expected."


# EMPTY DICTIONARY  
empty_dict={}

#wiping an existing dictionary (dictionary is mutable)

# programming_dictionary={}
# print(programming_dictionary)


# Editing a dictionary

programming_dictionary["Bug"]="A moth in your computer"

print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])