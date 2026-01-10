''' WARM UP PROBLEM'''

text="learning python is fun"
words=text.split()
words.reverse()
reversed_sentence = " ".join(words)
for ch in words:
    if ch in reversed_sentence:
        continue
print(reversed_sentence)


''' Given a sentence, reverse each word individually while keeping the word order the same,
remove extra spaces, and return the cleaned sentence '''

text = "  learning the python is fun  "

# remove extra spaces
text = text.strip()

# split into words
words = text.split()

reversed_words = []

# reverse each word
for word in words:
    reversed_word = ""

    for ch in word:
        reversed_word = ch + reversed_word

    reversed_words.append(reversed_word)

# join words with space
result = " ".join(reversed_words)

print(result)