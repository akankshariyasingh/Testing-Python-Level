'''
merge_problem_1.5 - Create a function that checks whether a string is a palindrome.

'''


def is_palindrome(text):
    rev=''
    for ch in text:
        rev=ch+rev
    return text==rev

print(is_palindrome("madam"))