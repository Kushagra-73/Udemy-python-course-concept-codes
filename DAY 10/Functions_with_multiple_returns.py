# Functions with multiple return statements
# Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))


