'''
adv_problem_1.3 - Return more frequent word in a sentence (ignore case and punctuation).

'''
def most_freq_word(text):
    text=text.lower()
    words=text.replace(",","").replace(",","").split() #remove punctuation and spaces.
    frequency={}
    for ch in words:
        if ch!=" ":
            if ch in frequency:
                frequency[ch]+=1
            else:
                frequency[ch]=1

    max_word="" #stores most frequent word
    max_count=0 #stores highest count

    for ch in frequency:
        if frequency[ch]>max_count:
            max_count=frequency[ch] 
            max_word=ch #update word
    return max_word #returns most frequent word

print(most_freq_word("Coding is therapy, Coding is fun."))

        

'''
Given a sentence, print the word that appears the least number of times.
'''

def least_freq_word(text):
    text=text.lower()
    words=text.replace(",","").replace(",","").split() #remove punctuation and spaces.
    frequency={}
    for ch in words:
        if ch in frequency:
            frequency[ch]+=1
        else:
            frequency[ch]=1     
               
    min_word="" #stores least frequent word
    min_count=float("inf") #initializes least count with a very large number.

    for ch in frequency:
        if frequency[ch]<min_count:
            min_count=frequency[ch] 
            min_word=ch #update word
    return min_word #returns most frequent word
   

print(least_freq_word("Coding is therapy, Coding is fun."))