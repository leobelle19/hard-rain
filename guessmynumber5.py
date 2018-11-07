'''
documentation
'''

import random

secret = random.randint(1, 99)

guess = 0
tries = 0
print("can you guess my number?")
print("My number is an integer between 1 and 99")

while guess != secret and tries < 6 :
    print("What is your guess?")
    guess = int(input())
    if guess < secret :
        print("Too low")
    elif guess > secret :
        print ("Too high")

    tries = tries + 1

if guess == secret:
    print("Congratulations Man! You Win!")
else :
    print(" Better luck next time")
    print("The secret number was : ", secret)

