'''WARM UP PROBLEMS'''

'''
PROBLEM 1 - Write a function that takes a list of numbers and return their sum.
'''

num=[3,6,8,3]
def calcultate(num):
    total=0
    for n in num:
        total+=n
    return total
print(calcultate(num))


'''
PROBLEM 2 - Write a function that counts in a string (ignore case)
'''

def vowel_count(text):
    text="python programming"
    vowel="aeiou"
    count=0
    for ch in text:
        if ch in vowel:
            count+=1
    return count
print(vowel_count("python programming"))

        
        
'''
PROBLEM 3 - Removes duplicates from a list while keeping order.
'''

def remove_duplicates(text):
    text="python programming"
    unique=[]
    for ch in text:
        if ch not in unique:
            unique.append(ch)
    return unique
print(remove_duplicates("python programming"))


'''
PROBLEM 4 - Returns the largest number from a list.
'''

def largest_number(lst):
    lst=[20,45,10,30]
    max_value=lst[0]
    for num in lst:
        if num > max_value:
            max_value=num
    return max_value
print(largest_number([20,45,10,30]))
        

'''
PROBLEM 5 - Checks whether a string is a palindrome.
'''

def is_palindrome(text):
    text="12321"
    rev=""
    for ch in text:
        rev=ch+rev
    return text == rev
print(is_palindrome("12321"))
