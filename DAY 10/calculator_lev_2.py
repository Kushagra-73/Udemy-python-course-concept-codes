from art import logo
print(logo)



continue_calculating=True
while continue_calculating:
    
    def add(n1, n2):
        return n1 + n2

    a=add(n1=first_number,n2=second_number)


    def subtract(n1,n2):
        if n2>n1:
            return n2-n1
        else:
            return n1-n2

    s= subtract(n1=first_number,n2=second_number)


    def multiply(n1,n2):
        return n1*n2

    m= multiply(n1=first_number,n2=second_number)


    def divide(n1,n2):
        return n1/n2

    d=divide(n1=first_number,n2=second_number)

    functions={"+":a,"-":s,"*":m,"/":d}


    first_number=int(input("Enter the first number :"))
    second_number=int(input("Enter the second number :"))
    
    

    result=int("")
    function_to_perform=input("What operation do you want to perform ? ")
    if function_to_perform in functions:
        result+=functions[function_to_perform]
        print(result)
        
        continue_operation=input("Do you want to continue calculation with your result ? 'yes' or 'no'").lower()
        if continue_operation=="yes":
            first_number=result
            result+=functions[function_to_perform]
            print(result)
    else:
        continue_calculating=False
    
    

        
        
  
