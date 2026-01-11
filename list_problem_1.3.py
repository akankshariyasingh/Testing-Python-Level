'''
list_problem_1.3 - Find the second largest number in the list without using sort()

'''

numbers=[10,40,20,30]

largest_number=numbers[0]

second_largest=numbers[0]

for num in numbers:
    if num > largest_number:
        second_largest=largest_number
        largest_number=num
    if num!=largest_number and num>second_largest:
        second_largest=num

print(second_largest)

        