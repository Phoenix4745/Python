import random

guesses_Taken = 0

my_Name = input()
print("Hello!, Welcome to My game " + my_Name)

secret_No = random.randint(1, 20)
print(my_Name + " I am thinking of a number between 1 and 20")
while guesses_Taken < 6:
    print('Take a guess')
    guess = input()
    guess = int(guess)

    guesses_Taken = guesses_Taken + 1

    if guess < secret_No:
        print("Your Guess is too low")

    if guess > secret_No:
        print("Your guess is too high")

    if guess == secret_No:
        break

if guess == secret_No:
    guesses_Taken = str(guesses_Taken)
    print("Congratulations! " + my_Name + " You guessed my number in " + guesses_Taken + " guesses!")

if guess != secret_No:
    secret_No = str(secret_No)
    print("Oh! I was thinking of " + secret_No)
