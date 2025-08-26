# My version
from art import logo

print(logo)

num1=float(input("Enter the first number :"))
num2=float(input("Enter the second number :"))
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

result=float()
operation=input(" \n +\n -\n *\n /\nWhat operation Do you want to perform? : ")
if operation in functions:
    result = functions[operation](num1, num2)
    # This is called dynamic function calling — you're choosing which function to run based on user input, 
    # and then calling it with arguments (num1, num2).
    print(f"{num1} {operation} {num2} = {result} ")
else:
    print("Invalid operation.")
    result = None

continue_calculating=True
while continue_calculating:
    
    choice=input(f"Do you want to continue calculation with {result} ? 'yes' or 'no' :").lower()
    if choice=="yes":
        num1=result
        num2=float(input(f"Enter another number to perform operation with {result} :"))
        operation=input("What operation Do you want to perform? :")
            
        if operation in functions:
            result=functions[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {result}")

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
