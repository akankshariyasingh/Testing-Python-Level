'''
adv_problem_1.2 - Merge two lists into one without duplicates and preserve order.

'''

def merge_list(list1, list2):
    result=[]
    for ch in list1+list2:   #loops through both list
        if ch not in result:
            result.append(ch)
    return result
print(merge_list([2,2,5,6],[3,4,5,2,7]))



'''
Given two lists, return a new list containing only the elements that appear in both lists.
'''

def merge_list(list1, list2):
    result=[]
    for ch in list1:   #loops through both list
        if ch not in result and ch in list2:
            result.append(ch)
    return result
print(merge_list([2,2,5,6],[3,4,5,2,7]))