import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = 'ant baboon bat bear beaver camel cat cobra crow deer dog donkey duck eagle fox frog goat goose hawk lion lizard llama monkey mouse mule owl panda parrot pigeon python rabbit ram rat raven rhino seal shark sheep sloth snake spider swan tiger toad turkey turtle whale wolf zebra'.split()


def getrandomword(wordlist):
    wordindex = random.randint(0, len(wordlist)-1)
    return wordlist[wordindex]


def displayboard(missedletters, correctletters, secretword):
    print(HANGMAN_PICS[len(missedletters)])
    print()

    print("Missed Letters:", end=' ')
    for letter in missedletters:
        print(letter, end=" ")
    print()

    blanks = '_' * len(secretword)

    for i in range (len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()


def checkGuess(alreadyguessed):
    while True:
        print("Give a guess")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please type a single letter")
        elif guess in alreadyguessed:
            print("Tou have already guessed this letter. Try again")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter")
        else:
            return guess


def playagain():
    print("Do you want to play again. (Yes or No) ")
    return input().lower().startswith("y")


print("H A N G M A N")
missedletters = ''
correctletters = ''
secretword = getrandomword(words)
gameIsDone = False

while True:
    displayboard(missedletters, correctletters, secretword)

    guess = checkGuess(missedletters + correctletters)
    if guess in secretword:
        correctletters = correctletters + guess
        foundAllLetters = True

        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes, the secret word is " + secretword + "!. And you have won")
            gameIsDone = True

    else:
        missedletters = missedletters + guess

    if len(missedletters) == len(HANGMAN_PICS)-1:
        print("You ran out of guesses \nAfter " +str(len(missedletters))+ " missed guesses and " + str(len(correctletters))+
        " correct guesses. The word was " + secretword)

        gameIsDone = True

    if gameIsDone:
        if playagain():
            missedletters = ''
            correctletters = ''
            secretword = getrandomword(words)
            gameIsDone = False

        else:
            break



