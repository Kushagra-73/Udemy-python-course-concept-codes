def greet():
    print("HEY !")
    print("Good morning ")
    print("How are you doing ")


greet()

greet()

def function(something):
    # Do this with something
    # Then do this 
    pass

# Function that allows input

def greet_with_name(name):         # Here name is parameter 
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Anika")           # Anika is argument

# Functions with multiple inputs
def greet_with_n_a_L(name,location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

greet_with_n_a_L("Anika","Tokyo")
