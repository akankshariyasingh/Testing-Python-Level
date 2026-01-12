'''
loops_problem_1.2 - Given a list of numbers, count how many are even and how many are odd using a for loop.

'''


numbers=[2,4,5,8,3]

even_count=0

odd_count=0

for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
        
print(f"Even number in list:{even_count}")
print(f"Odd number in list:{odd_count}")