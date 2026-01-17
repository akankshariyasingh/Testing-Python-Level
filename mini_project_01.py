'''
mini_project_01 - Text Analyzer Tool
1. Normalize text(lowercase,remove punctuation)
2. count word freuency
3. find most and least frequent word
4. remove duplicates words (keep order)
5. Return all results using functions + dictionaries +lists +loops

'''

def analyze_text(sentence):
    sentence=sentence.lower()
    words=sentence.replace(",","").replace(",","").split()
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    
    max_word=None
    min_word=None
    max_count=float("-inf")
    min_count=float("inf")
    
    for word in frequency:
        if frequency[word]>max_count:
            max_count=frequency[word]
            max_word=word
        if frequency[word]<min_count:
            min_word=frequency[word]
            min_word=word
    
    seen=set()
    unique=[]
    for word in words:
        if word not in seen:
            unique.append(word)
            seen.add(word)
    
    return{ "freq": frequency, "most_freq":max_word, "least_freq":min_word,"unique_words":unique }

print(analyze_text("python programming python is fun"))