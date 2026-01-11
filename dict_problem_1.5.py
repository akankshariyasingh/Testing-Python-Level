'''
dict_problem_1.5 - Given a dictionary of users and their ages, create a new dictionary containing only 
valid users( age between 18 and 60 ).

'''

users={"Akanksha":20,"Rahul":17,"Neha":65,"Ankit":30}
result={}
for name in users:
    age=users[name]
    if age<=60 and age>=18: #will not write else because we just want valid users
        result[name]=age
print(result)
