'''
some_more_1.1 - Given a list of integers, find the lenght of the longest consecutive sequence (order does 
  not matter).

'''

def longest_consecutive_sequence(lst):
    consecutive_num=set(lst) #made list a set contains the unique value in it.
    longest=0 #contain the length of longest sequence.
    for num in consecutive_num:   #take set not list coz we converted the list into set.
        if num-1 not in consecutive_num:  #num-1 not present means no smaller consecutive number is exist
            length=1  #count the sequence length form 1 coz number in itself is counted.
            while num + length in consecutive_num:  #still keeps checking for the next consecutive number. 
                length +=1 #increases the sequence by 1
                longest=max(longest,length) #updates longest with max sequence found so far
            
    return longest

print(longest_consecutive_sequence([100,2,200,3,4]))
