'''
adv_problem_1.1 - Create a function that returns the first charater in a string that does not repeat.
(ignore case).

'''

def first_char(text):
    text=text.lower()
    unique={}
    for ch in text:
        if ch!= " ":  #skips spaces in between words inside the string
            if ch in unique:
                unique[ch]+=1
            else:
                unique[ch]=1
    for ch in text:
            if ch!=" " and unique[ch]==1:  #find first unique character
                 return ch #return that character
    
    return None #return None if none found

print(first_char("python programming"))