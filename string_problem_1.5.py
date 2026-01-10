''' Given a password, check whether it has at least 8 characters, one uppercase letter, one
lowercase letter,one digit, and one special character.
'''

password = "Ak@12345"
upper = False
lower = False
digit = False
special = False
for ch in password:
    if ch>="A" and ch<="Z":
        upper=True
    elif ch>="a" and ch<="z":
        lower=True
    elif ch>="0" and ch <="9":
        digit=True
    elif ch=="@" or ch=="#" or ch=="$" or ch=="%" or ch=="!":
        special=True
if len(password)>=8 and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")

