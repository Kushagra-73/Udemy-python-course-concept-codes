# Functions with multiple return statements
# Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

"""
| Code                                  | What it does                                      |
| ------------------------------------- | ------------------------------------------------- |
| `functions[operation]`                | Fetches the function (like `add`)                 |
| `functions[operation](x, y)`          | **Calls** the function with arguments `x` and `y` |
| `result = functions[operation]`       | Stores the function itself, not the result        |
| `result = functions[operation](x, y)` | Stores the result of running the function         |
"""


def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))


