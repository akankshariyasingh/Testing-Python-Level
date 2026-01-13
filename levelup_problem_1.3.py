'''
levelup_problem_1.3 - Create a function that returns only duplicate characters 
with their count from a string.

'''

def duplicate_char(text):
    freq={}
    duplicate={}
    for ch in text:
        if ch != " ":
            freq[ch]=freq.get(ch,0)+1
    for ch in freq:
        if freq[ch]>1:
            duplicate[ch]=freq[ch]
    return duplicate

print(duplicate_char("python programming"))
            