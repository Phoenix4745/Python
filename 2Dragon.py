import random
import time


def display_intro():
    print('You are in a land of dragons')
    print('It is dark and spooky')
    print('The dragon will eat you up or share his treasure with you')


def choose_cave():
    cave = ' '
    while cave != "1" and cave != "2":
        print('In which cave do you want to go (1 or 2)')
        cave = input()

    return cave


def check_cave(chosen_cave):
    print('You went inside the cave...')
    time.sleep(2)
    print('It was very dark and spooky...')
    time.sleep(2)
    print('A large dragon comes before you. He opens his jaws and...')
    print()
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if int(chosen_cave) == friendly_cave:
        print("He gives you treasure!")

    else:
        print("He eats you up")

play_again = "yes"

while play_again == 'yes' or play_again == "y":
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print("Do you want to play again (Yes or No)")
    play_again = input()
