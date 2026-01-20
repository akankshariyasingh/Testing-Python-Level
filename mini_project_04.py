'''
mini_project_04 - Smart Number Analyzer

Take a number from the user and analyze them using basic logic (using print function).
1. even/odd
2. maximum/minimum
3. average
4. prime numbers
5. numbers greater than average

'''

numbers=list(map(int,input("Enter numbers seperated by space").split()))
print("Total number",len(numbers))

even_number=[]
odd_number=[]
for num in numbers:
    if num%2==0:
        even_number.append(num)
    else:
        odd_number.append(num)
print("Even_number",even_number)
print("Odd_number",odd_number)

average=sum(numbers)/len(numbers)
print("Average",average)

prime_number=[]
for num in numbers:
    if num>1:
        is_prime=True
        for i in range(2,num):
            if i%2==0:
                is_prime=True
                break
        if is_prime:
            prime_number.append(num)
print("Prime Number",prime_number)
    
greater_than_avg=[]
for num in numbers:
    if num>average:
        greater_than_avg.append(num)
print("Number greater than average:",greater_than_avg)



        
    
    

            
        

