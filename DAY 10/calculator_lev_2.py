from art import logo
print(logo)

first_number=float(input("Enter the first number :"))
second_number=float(input("Enter the second number :"))
def add(n1, n2):
        return n1 + n2

def subtract(n1,n2):
    if n2>n1:
        return n2   -n1
    else:
        return n1-n2


def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Not defined"

functions={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }

result=int()
operation=input(" \n +\n -\n *\n /\nWhat operation Do you want to perform? : ")
if operation in functions:
    result = functions[operation](first_number, second_number)
    # This is called dynamic function calling — you're choosing which function to run based on user input, 
    # and then calling it with arguments (first_number, second_number).
    print(f"The final result is = {result} ")
else:
    print("Invalid operation.")
    result = None

continue_calculating=True
while continue_calculating:
    
    continue_operation=input("Do you want to continue calculation with your result ? 'yes' or 'no' :").lower()
    if continue_operation=="yes":
        first_number=result
        second_number=float(input("Enter another number to perform operation with :"))
        operation=input("What operation Do you want to perform? :")
            
        if operation in functions:
            result=functions[operation](first_number, second_number)
            print(f"final result is = {result}")

        else:
            print("Invalid operation.")
            continue_calculating=False
    
    else:
        continue_calculating=False
    
"""
| Code                                  | What it does                                      |
| ------------------------------------- | ------------------------------------------------- |
| `functions[operation]`                | Fetches the function (like `add`)                 |
| `functions[operation](x, y)`          | **Calls** the function with arguments `x` and `y` |
| `result = functions[operation]`       | Stores the function itself, not the result        |
| `result = functions[operation](x, y)` | Stores the result of running the function         |
"""

    
        
  
