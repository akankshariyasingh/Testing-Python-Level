'''
merge_problem_1.1 - Create a function that takes a sentence and returns a dictionary of word frequencies
(ignore case).
'''


def word_frequency(text):
    frequency={}
    text=text.lower()
    for ch in text:
        if ch in frequency:
            frequency[ch]=frequency[ch]+1
        else:
            frequency[ch]=1
    return frequency

print(word_frequency("coding is fun and coding is learning"))
