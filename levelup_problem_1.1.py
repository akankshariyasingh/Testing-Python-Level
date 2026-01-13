'''
levelup_problem_1.1 - Create a function that returns the most frequent word in a sentence(ignore case
& punctuation).

'''


def most_frequent_word(sentence):
    sentence=sentence.lower()
    words=sentence.replace(",","").replace(".","",).split()
    most_occuring_word={}
    for ch in words:
        if ch in most_occuring_word:
            most_occuring_word[ch]+=1
        else:
            most_occuring_word[ch]=1

    max_word="" #store most frequent word
    max_count=0 #store highest frequency

    for ch in most_occuring_word:
        if most_occuring_word[ch]>max_count:
            max_count=most_occuring_word[ch]
            max_word=ch

    return max_word
print(most_frequent_word("Python is fun, and Python is powerful."))