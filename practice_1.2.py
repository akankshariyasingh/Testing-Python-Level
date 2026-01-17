'''
practice_1.2 - Find the majority elements in a list.'''

def max_elements(lst):
    frequency={}
    for num in lst:
        frequency[num]=frequency.get(num,0)+1
    for key in frequency:
        if frequency[key]>len(lst)//2:  #len(lst)//2 = half of the list is obviously majority
            return key #return majority element
    
    return None

print(max_elements([1,2,1,1,3,2]))