''' Given an email address, mask all characters before @ except the first two characters.'''

email = "akanksha.singh@gmail.com"
username,domain=email.split("@")
masked_username=""
for i in range(len(username)):
    if i<2:
        masked_username+=username[i]
    else:
        masked_username+="*"
masked_mail=masked_username+"@"+domain
print(masked_mail)


