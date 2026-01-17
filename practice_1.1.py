'''
practice_1.1 - Given a string, return the first character that does not repeat. If none exists,return None.

'''

def first_non_rep_ch(text):
    result={}
    for word in text:
        result[word]=result.get(word,0)+1 #count each word
    for word in text:
        if result[word]==1:    #checks non repeating word
            return word
    return None

print(first_non_rep_ch("aabbcde"))




