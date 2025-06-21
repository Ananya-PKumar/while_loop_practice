#2. Guessing game
import random

secret_number = random.randint(1,10)
while True:
    try:
        guess = int(input("please guess a random number between 1-10"))
        break
    except ValueError:
        print("please input a number only (between 1-10).")

while guess != secret_number:
    try:
        guess = int(input("incorrect! try again!"))
    except ValueError:
        print("please input a number only (between 1-10).")
print(f"yay you got the secret number, {secret_number}! congrats.")
