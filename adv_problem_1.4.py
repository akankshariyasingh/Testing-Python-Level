'''
adv_problem_1.4 - Returns a dictionary with count of digits and letters in a string

'''

def count_digits_letters(text):
    result={"digits":0,"letters":0}  #initializes dictionary
    for ch in text:
        if ch.isdigit(): #when we wants to check the digits. (write direct in if line itself coz it tells the condition)
            result["digits"]+=1
        elif ch.isalpha():  #when we want to check the letters.
            result["letters"]+=1
    return result

print(count_digits_letters("pyhton programming is 1000 times fun."))
        
