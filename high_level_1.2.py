'''
high_level_1.2- Given a list of sentences, return words that appear in every sentence (case-insensitive).

'''

def common_words(sentences):
    common=set(sentences[0].lower().split()) 
    '''
    sentence[0]= start with first sentence index 0 "python is fun"
    split()= python is fun. split the first sentence.
    '''
    
    for word in sentences[1:]: 
        common&= set(word.lower().split())
    return list(common)

  
print(common_words(["Python is programming", "python is fun","i love python"]))

'''
sentence[1:]=will iterate with the all the sentence from index 1 coz already covered index 0
common word for both rest sentence.
&= means set interaction with each other and update. keeps only those words that keeps in both the sets.
''' 