def is_prime(num):
    if num<=1:
        return False
        
    for i in range(2,num):    # for num=2 i.e. range(2,2) the loop doesnt work therefore it comes out to be True
        if num%i==0:
            return False
        
    
    return True
        
print(is_prime(2))
print(is_prime(75))