guess_left= 3 

print("Counting...")
while guesses_left > 0 :
    guess = int (input('your guess: '))
    if guess == random_number:
        print('you win')
        break
    guess_left -= 1
else: 
    print('you lose')
for i in range(10):
    print(i)
