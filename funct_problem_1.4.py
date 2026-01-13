'''
func_problem_1.4 - Create a function that returns the second largest number from the list(without using sort()).
'''


def second_largest_num(lst):
    largest_number=second_largest_num=float('-inf')  #smallest than any real nnumber so no matter what numbers
                                                       # come in the list, they will be bigger than -inf.
    for num in lst:
        if num>largest_number:
            second_largest_num=largest_number
            largest_number=num
        elif num>second_largest_num:
            second_largest_num=num
    return second_largest_num

print(second_largest_num([20,40,30,10]))