import sys
import random


def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)

# get your team & get your board
team = input()
first_row = input()
second_row = input()
third_row = input()

# print out the inputs you're getting
debug_print(team)
debug_print(first_row)
debug_print(second_row)
debug_print(third_row)

# Outputting the coordinates of your board
if random.random() > .5:
    print("0 1")
else:
    print("0 0")
