'''
high-level_1.3 - Return the first word that appears only once in a sentence.

'''

def first_word(sentence):
    words=sentence.lower().split()  #converts sentence to word list (line takes time)
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    for word in words:
        if frequency[word]==1: #checks unique word
            return word  #return first unique word
        
    return None

print(first_word("python is amazing language to learn so learn python"))
