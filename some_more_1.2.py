'''
some_more_1.2 - Group words that have same characters.

'''
    
def group_word(lst):
    result={}
    for ch in lst:
        key="".join(sorted(ch.lower())) #sort the letters of words alphabetically and returns a list of ch.
        # "".join(...) joins the sorted characters back into one string.
        # key=unique identifier words form the same letters
        result[key]=result.get(key,[])+[ch] 
        # [] means if key does not exist it returns the list[] empty
    return list(result.values()) #returns only the lists of grouped words

print(group_word(["eat","tea","tan","ant"]))