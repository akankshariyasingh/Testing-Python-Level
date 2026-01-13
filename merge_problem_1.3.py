def character_count(text):
    frequency={}
    for ch in text:
        if ch != " ":
            if ch in frequency:
                frequency[ch]+=1
            else:
                frequency[ch]=1
    return frequency
print(character_count("python programming"))



'''
character count

'''

def frequency_count(text):
    word=text.strip()
    count=0
    for ch in text:
        if ch in word:
            count+=1
        else:
            count=1
    return count
print(frequency_count("python programming"))