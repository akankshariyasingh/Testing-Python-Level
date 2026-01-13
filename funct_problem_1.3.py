'''
funct_problem_1.3 - Create a function that checks whether a number is a perfect number ( A number whose
divisors sum equals the number itself).

'''

def perfect_number(num):
    total=0
    for i in range(1,num):
        if num%i==0:
            total+=i
    return total==num

print(perfect_number(28))