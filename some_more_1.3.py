'''
some_more_1.3 - Returns the first word that appears only once in a sentence.
'''
def first_word(sentence):
    words=sentence.lower().split()
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    for word in words:
        if frequency[word]==1:
            return word
    return None
print(first_word("coding is fun and i love coding"))
    
