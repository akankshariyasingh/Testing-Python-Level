'''
dict_problem_1.6 - Given a string, create a dictionary that stores the frequency of each character,ignoring
spaces and case.

'''

text="Python Programming"

ferquency={}

text=text.lower() #for lower case

words=text.strip() #for space inside the string

for words in text:
    if words in ferquency:
        ferquency[words]=ferquency[words]+1
    else:
        ferquency[words]=1
        
print(ferquency)