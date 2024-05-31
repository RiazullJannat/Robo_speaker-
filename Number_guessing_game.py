import random
import math

# Taking inputs
lower = int(input("Enter lower bound:- "))
upper = int(input("Enter upper bound:- "))
# generating random number between the lower and upper.

x = random.randint(lower,upper)
print(f"\n\tYou've only {round(math.log(upper-lower+1,2))} chances to guess the integer")

# Initializing the number of guesses.
count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1
    # Taking guessing number
    guess = int(input("Guess a number:- "))
    # condition for testing
    if guess == x:
        print(f"Congratulations you did it in {count} try.")
        break
    elif guess > x:
        print("You guessed too high.")
    elif guess < x:
        print("You guessed too small.")
# If guessing is more than required guesses shows this output.

if count >= math.log(upper - lower + 1,2):
    print(f"\nThe number is {x}")
    print("\tBetter luck next time.")

