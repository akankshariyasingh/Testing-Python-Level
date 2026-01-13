'''
funct_problem_1.6 - Cretae a function that removes duplicate characters from a string while keeping
original order.
'''



def remove_duplicates(unique):
    text="python programming"
    unique=[]
    for ch in text:
        if ch not in unique:
            unique.append(ch)
    return unique

print(remove_duplicates("python programming"))

