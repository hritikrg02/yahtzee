"""
file: yahtzee.py
description: simulates rolling a yahtzee
language: python3
author: Hritik "Ricky" Gupta
"""

from random import randint as r
from time import time

def die_roll(sides, no_dice):
    """
    rolls a number of dice with a given number of sides
    :param sides: number of sides of one die (int)
    :param no_dice: number of dice to be rolled (int)
    :return: dictionary with rolls
    """
    rolls = {}
    for i in range(int(no_dice) + 1):
        key_name = 'die' + str(i)
        roll = r(1, int(sides))
        rolls[key_name] = roll
    return rolls

def check_rolls(rolls):
    """
    checks rolls to see there is a yahtzee
    :param rolls: dictionary containing each die with its respective roll
    :return: True if yahtzee is found, False otherwise
    """
    number = list(rolls.values())[0]
    for roll in rolls:
        current_roll = rolls[roll]
        if current_roll != number:
            return False, number
    return True, number


def main():
    """
    runs die_roll and check_rolls until a yahtzee is found
    and then prints the number of rolls and the number rolled to the user
    as well as how long the operation took
    """
    sides = input("How many sides would you like the die to have? ")
    no_dice = input("How many dice are there? ")
    no_rolls = 0
    t0 = time()

    while True:
        rolls = die_roll(sides, no_dice)
        yahtzee, number = check_rolls(rolls)
        if yahtzee is True:
            break
        else:
            no_rolls += 1

    t1 = time()
    total_time = (t1 - t0) * 1000
    print("Got a yahtzee for the number", str(number), "after", str(no_rolls), "rolls", '(took', total_time, 'ms)')

if __name__ == '__main__':
    main()
