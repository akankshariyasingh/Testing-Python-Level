'''
list_problem_1.1 - Given a list of integers, create a new list that removes duplicates without changing
the original order.

'''

numbers=[1,2,2,3,3,4,5,4,6]

result=[]

for num in numbers:
    if num  not in result:
        result.append(num)

print(result)
