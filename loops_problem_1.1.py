'''
loops_problem_1.1 - Given a list of integers, create a new list that contains only numbers greater than 10.

'''

integers=[1,3,9,20,35,4,20,45]

result=[]

for num in integers:
    if num>10:
        result.append(num)

print(result)