'''
some_more_1.4 - Remove duplicates without changing order.
'''

def remove_duplicates(sentence):
    words=sentence.lower().split()
    duplicate=[]
    for word in words:
        if word not in duplicate:
            duplicate.append(word)
    return " ".join(duplicate) 

print(remove_duplicates("Coding is therapy and coding is fun."))
 
