import random

print ("Number guessing game")

number = random.randint(1,9)

chances = 0

print ("Guess a number between (1 to 9)")

while chances < 5 :

    guess = int(input("Enter your guess : "))

    if guess == number :
        print ("Congrats You Won")
        break

    elif guess < number :
        print ("The number you have choosen is too low, Guess a higher number")

    else :
        print ("The number you have choosen is too high, Guess a lower number")

    chances += 1

if not chances < 5:
    print ("You Lose (Sorry), The number is", number)
