'''
loops_problem_1.4 - Given a list that removes duplicates but keep the original order.

'''


text=("Coding is a therapy")

text=text.strip()

unique_list=[]

for word in text:
    if word==' ':
        continue

for word in text:
    if word not in unique_list:
        unique_list.append(word)
print(unique_list)


