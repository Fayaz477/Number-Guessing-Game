import random
n=random.randint(1,10)
print("Welcome to number guessing game")
print("This is a number guessing game Where you can guess a number betwen 1 and 10")
print("if guessed number is correct you winned the game you have only 3 chances")
print("Lets play!")
guesses=[0]
i=0
while True:
    if i<3:
        guess=int(input("Enter guess number:"))
        if guess<1 or guess>10:
            print("Enter a number 1 and 10")
            continue
        elif guess==n:
            print("Congragulations You guesed is right you winned the game")
            break
    #depending on the condition whether the number is greater or lesser
        if guess>n:
            print('The value is greater')
        else:
            print("Value is lesser")
    
        
        i+=1
    else:
        print("your chances is over the corect number is",n)
        break
