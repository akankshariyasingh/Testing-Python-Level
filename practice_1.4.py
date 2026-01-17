'''
practice_1.4 - Reverse each word, not the sentence order.
'''

def reverse_each_ch(text):
    words=text.split()
    reversed=[]
    for word in words:
        reversed.append(word[::-1]) #using indexing
    return " ".join(reversed)

print(reverse_each_ch("I love Python"))