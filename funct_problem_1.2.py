'''
funct_problem_1.2 - Create a function that takes a sentence and returns a dictionary containing the 
frequency of each word ( ignore case )

'''

def words_frequency(text):
    text="coding is a therapy"
    frequency={}
    for ch in text:
        if ch in frequency:
            frequency[ch]+=1
        else:
            frequency[ch]=1
    return frequency

print(words_frequency("coding is a therapy"))