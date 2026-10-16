import random

guesses_left = 3
random_number = random.randint(1, 10)

print("Counting...")

while guesses_left > 0:
    guess = int(input("Your guess: "))

    if guess == random_number:
        print("You win!")
        break
    else:
        guesses_left -= 1
else:
    print("You lose.")
