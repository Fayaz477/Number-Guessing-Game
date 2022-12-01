import random
n=random.randint(1,10)
print("Welcome to number guessing game")
print("This is a number guessing game Where you can guess a number betwen 1 and 10")
print("if guessed number is correct you winned the game you have only 3 chances")
print("Lets play!")
guesses=[0]
while True:
    guess=int(input("Enter guess number:"))
    if guess<1 or guess>10:
        print("Enter a number 1 and 10")
        continue
    elif guess==n:
        print("Congragulations You guesed is right you winned the game")
        break
    #if guessed number is incorrect save it in another list
    guesses.append(guess)
    if len(guesses)>3:
        print("your chances is over The number is:",n)
        break
    else:
        print("you guessed number is incorrect try again")
