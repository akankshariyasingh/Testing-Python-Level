'''
merge_problem_1.4 - Create a function that returns the largest number from a list without using max().

'''


def largest_number(lst):
    largest=lst[0]
    for num in lst:
        if num>largest:
            largest=num
    return largest

print(largest_number([10,30,40,20]))



'''
Create a function that returns the second largest number from a list without using max().

'''

def second_largest_number(lst):
    largest=second_largest_number=float('-inf')
    for num in lst:
        if num>largest:
            second_largest_number=largest
            largest=num
        elif num>second_largest_number and num!=largest:
            second_largest_number=num
    return second_largest_number

print(second_largest_number([10,30,40,20]))