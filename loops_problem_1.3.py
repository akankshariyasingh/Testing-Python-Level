'''
loops_problem_1.3 - Given a string, how many times each character appears using a for loop(ignore spaces).

'''


text=(" Python Programming ")
text=text.strip()

result={}
for word in text:
    if word==' ':
        continue

    if word in result:
        result[word]+=1
    else:
        result[word]=1

print(result)