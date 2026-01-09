'''
string_problem_1.1 - Given a list of usernames, remove spaces,convert to lowercase, and 
keep only usernames containing letters, digits and underscores.

'''

usernames=[" akanksha_123 ","Rahul@", "neha__99", "Ankit!", "valid_user "]
valid_usernames=[]
for name in usernames:
    name=name.strip().lower()
    if name=="":
        continue
    is_valid=True
    for ch in name:
        if not (ch.isalpha() or ch.isdigit() or ch=="_"):
            is_valid=False
            break
    if is_valid:
        valid_usernames.append(name)
     
print(valid_usernames)