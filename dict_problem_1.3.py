'''
dict_problem_1.3 - Given a dictionary of students and their cities, invert it so cities become keys
and values are lists of students.

'''

students={"Akanksha":"Bhopal","Rahul":"Indore","Neha":"Bhopal","Ankit":"Indore"}

result={} #to store the new dictioinary  

for name in students:
    city=students[name]
    if city in result:
        result[city].append(name)   # to insert the name if you add +1 it will give the cities count
    else:
        result[city]=[name]

print(result)

    
