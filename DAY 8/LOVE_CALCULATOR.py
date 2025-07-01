def calculate_love_score(name1,name2):
    com_name=(name1+name2).lower()
    
    t=com_name.count("t")
    r=com_name.count("r")
    u=com_name.count("u")
    

    l=com_name.count("l")
    o=com_name.count("o")
    v=com_name.count("v")
    e=com_name.count("e")
    true=t+r+u+e
    love=l+o+v+e

    print(f"Your love score is {true}{love}")

calculate_love_score("Kushagra","Vaanya")
