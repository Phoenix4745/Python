import random


def welcome():
    print('Welcome, What is your name ?')
    Pname = input().title()
    print('Welcome ' + Pname + ' To my game Stone Paper Scissor. Let\'s play ')


choice = ['stone', 'paper', 'scissor']


def getRandomMove(Move):  #Computer chooses move
    choice_index = random.randint(0, 2)
    return Move[choice_index]


def display(PPoints, CPoints):
    print("Stone Paper Scissor")
    print("Player's Points: ", PPoints, "Computer's Points: ", CPoints)


def getguess():  # Getting the player's choice
    print("Enter your move")
    playermove = input()
    playermove = playermove.lower()
    if playermove not in choice:
        print("Enter a valid response")
    else:
        return playermove


def playagain():
    print('Do you want to playagain. (Yes or No)')
    return input().lower().startswith("y")


PPoints = 0
CPoints = 0
gameIsDone = False
welcome()

while True:
    CompMove = getRandomMove(choice)
    if PPoints == 5:
        print("You won!. You beat the computer by " , (PPoints-CPoints) , " points")
        gameIsDone = True
        if gameIsDone:
            if playagain():
                PPoints = 0
                CPoints = 0
                gameIsDone = False
            else:
                break

    elif CPoints == 5:
        print("You Lose :( . You lost by " , (CPoints-PPoints) , " points")
        gameIsDone = True
        if gameIsDone:
            if playagain():
                PPoints = 0
                CPoints = 0
                gameIsDone = False
            else:
                break
    display(PPoints, CPoints)
    playermove = getguess()
    if CompMove == playermove:
        print('Tie')

    elif playermove == "stone":
        if CompMove == "paper":
            print('You lose, Computer chose paper and gets 1 point')
            CPoints = CPoints + 1
        else:
            print("You win, Computer chose scissor and you get 1 point")
            PPoints = PPoints + 1

    elif playermove == "paper":
        if CompMove == "scissor":
            print('You lose, Computer chose scissor and gets 1 point')
            CPoints = CPoints + 1
        else:
            print("You win, Computer chose stone and you get 1 point")
            PPoints = PPoints + 1

    elif playermove == "scissor":
        if CompMove == "stone":
            print('You lose, Computer chose stone and gets 1 point')
            CPoints = CPoints + 1
        else:
            print("You win, Computer chose paper and you get 1 point")
            PPoints = PPoints + 1
