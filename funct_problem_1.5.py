'''
func_problem_1.5 - Create a function that checks if a password: 
1. has at least 8 characters 
2. contains a digit
3. contains an uppercase letter
'''

def strong_password(password):
    has_digit=False
    has_upper=False
    if len(password)<8:
        return False
    for ch in password:
        if ch.isdigit():
            has_digit=True
        elif ch.isupper():
            has_upper=True
    return has_digit and has_upper

print(strong_password("akan1234"))
        

    

