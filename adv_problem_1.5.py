'''
adv_problem_1.5 - Check if two strings are Anagrams ( same characters,same count)

'''

def is_anagrams(text1,text2):
    text1=text2.replace(" ","").lower()
    text2=text2.replace(" ","").lower()

    if len(text1)!=(text2):
        return False
    
    result={}

    for ch in text1:
        result[ch]=result.get(ch,0)+1
    
    for ch in text2:
        if ch not in result or result[ch]==0:
            return False
        
        result[ch]-=1

    return True

print(is_anagrams("listen","silent"))

