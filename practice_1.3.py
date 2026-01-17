'''
practice_1.3 - Check whether one list is a rotation of another.

'''

def rotation_list(list1,list2):
    if len(list1)!=len(list2):
        return False
    for i in range(len(list1)):  
        if list1[i:]+list1[:i]==list2:    #a[i:]= i se end tak  and a[:i]= end se i-1 tak
            return True

print(rotation_list([1,2,3,4],[3,4,1,2]))
