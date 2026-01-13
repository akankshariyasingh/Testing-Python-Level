'''
levelup_problem_1.2 - Create a function that returns a dictionary where keys are list elements and value
are their index positions.

'''


''' METHOD 1 USING ENUMERATE'''
def key_value(lst):
    result={}
    for index,value in enumerate(lst):     # enumerate gives the ( index, value ) together            
        result[value]=index   
    return result
print(key_value(["a","b","c"]))


''' METHOD 2 USING LOOP '''
def key_value(lst):
    result={}
    for i in range(len(lst)):        #loop using index which is i     
        result[lst[i]]=i  #maps elements to its index which means provide its value with respect to its index
    return result
print(key_value(["python","java","c++"]))