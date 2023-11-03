# Number Guessing Game in Python

import random
import math

lower = int(input("Enter low : "))
higher = int(input("Enter High : "))

if higher <= lower:
    print("Enter Valid range...")
    exit()

number = random.randint(lower, higher)

print("\n\tYou've only ", 
       round(math.log(higher - lower + 1, 2)),
      " chances to guess the integer!\n")

# no of guesses
count = 0

while count < math.log(higher - lower + 1, 2):
    count += 1

    guess = int(input("Enter your guess : "))

    if number == guess:
        print("You got it in " + str(count) + " guesses.")
        break

    elif number > guess:
        print("You guessed it low...")
    
    else:
         print("You guessed it high...")

if count > math.log(higher - lower + 1, 2):
    print("\nThe number is %d" % number)
    print("\tBetter Luck Next time!")
    
