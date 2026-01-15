'''
high_level_1.4 - Merge two lists and keep only duplicates(frequency>=2.)
'''

def duplicate_elements(lst1,lst2):
    duplicates={}
    for word in lst1+lst2:
        if word in duplicates:
            duplicates[word]+=1
        else:
            duplicates[word]=1
    result=[] #put the duplicates word by assigining a new list of storage and define the external condition there.
    for word in duplicates:
        if duplicates[word]>1:
            result.append(word)
    return result

print(duplicate_elements([1,2,3,4,5],[1,3,5]))
    