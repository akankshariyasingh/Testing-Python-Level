'''WARM UP PROBLEM'''

sentence="AI is the future and AI is powerful"
frequency={}
words=sentence.split()
for word in words:
    frequency[word] = frequency.get(word,0)+1
print(frequency)
        

''' 
string_problem_1.2 - Given a paragraph, convert it to lowercase, remove punctuation, count
how many times each word appears, and print only the words that occur more than once.
'''

text="AI is the future. AI, and Machine Learning are the future of AI!"
text=text.lower()
punctuation_marks=".,!?"
for ch in punctuation_marks:
    text=text.replace(ch,"")

words=text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word,0)+1

result={}

for word, count in frequency.items():
    if count>1:
        result[word]=count
print(result)