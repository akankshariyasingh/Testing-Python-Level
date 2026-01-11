'''
list_problem_1.2 - Given a list of elements, count how many times each element appears and store the 
result in a dictionary.
'''


fruits=["apple","banana","apple","orange","orange","apple"]

frequency={}

for fruit in fruits:
    if fruit in frequency:
        frequency[fruit]+=1
    else:
        frequency[fruit]=1       

print(frequency)