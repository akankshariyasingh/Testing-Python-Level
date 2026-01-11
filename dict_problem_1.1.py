'''
dict_problem_1.1 - Given a list of(name, score) pairs, combine scores of the same person (case-insensitive)
into a dictionary.

'''

data={"Akanksha":80,"rahul":70,"AKANKSHA":90,"Rahul":85}

result={}

for name in data:
    score=data[name]
    name=name.lower()
    
    if name in result:
        result[name]=result[name]+score
    else:
        result[name]=score

print(result)




