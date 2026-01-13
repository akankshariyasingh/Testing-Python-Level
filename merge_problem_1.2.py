'''
merge_problem_1.2 - Create a function that removes duplicates from a list without using a set() and 
preserves order.

'''


def remove_duplicates(lst):
    unique=[]
    for ch in lst:
        if ch not in unique:
            unique.append(ch)
    return unique
print(remove_duplicates([1,3,4,2,1,2,1]))