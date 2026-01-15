'''

high_level_1.1 - Create a function that takes a list of integers and returns the most frequent even number.
If no even number exists, return None.

'''

def most_frequent_even_number(lst):
    
    frequency={} #It will store Key (an even number) and Value (how many times that even number appears)
    for num in lst:
        if num%2==0:
            frequency[num]=frequency.get(num,0)+1 #(num=current count of num) and (0= if num is not already in the dict.)
    if not frequency:
        return None
    
    return max(frequency,key=frequency.get)  #line takes time 
    
'''
max()= find the key with the highest value.
key=frequency.get tells python:" compare dictionary keys based on their frequency(values), not the key itself."
'''
print(most_frequent_even_number([2,3,6,6]))


