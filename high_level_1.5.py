'''
high_level_1.5 - Sentence is valid if it contains at least 1 uppercase letter, 1 digit and length should be 
>=8 Return True or False.

'''

def valid_sentence(sentence):
    result=[]
    if len(sentence)<8:
        return False
        
    for word in sentence:
        if word.isdigit():
            result.append("digit")
        elif word.isupper():
            result.append("uppercase")
        return True
    return result

print(valid_sentence("Akank123"))