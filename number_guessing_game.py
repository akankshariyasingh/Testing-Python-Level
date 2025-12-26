import random
print("welcome to the number guessing game!")
system_guess=random.randint(1,100)
print("DEBUG: system_number detected=", system_guess) #to see the system number
while True:
    user_guess=int(input("enter the number"))
    if system_guess>user_guess or system_guess<user_guess:
        print("you are too close to the number")
    elif system_guess==user_guess:
        print("Congratulations! you guess the number.")
        break
    else:
        print("invalid input")
