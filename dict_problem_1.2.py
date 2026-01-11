'''
dict_problem_1.2 - Given a list of logins (username,device), create a case-sensitive dictionary where each 
usermaps to another dictionary counting how many times they logged in from each device.
'''


logins=[("Akanksha","mobile"),("akanksha","laptop"),("RAHUL","mobile"),("rahul","mobile"),("Akanksha","mobile")]

sorted_dictionary={}

for name,device in logins:  #unpacking
    name=name.lower()        #convert all into lowercase
    
    if name not in sorted_dictionary:
        sorted_dictionary[name]={}       #create inner dictionary we are using two brackets here
    
    if device in sorted_dictionary[name]:
        sorted_dictionary[name][device]=sorted_dictionary[name][device]+1
    else:
        sorted_dictionary[name][device]=1
    
print(sorted_dictionary)
    