# Guess the right random number in 10 guesses
import random
n = random.randint(1,100)

a = -1
guesses = 1

while(guesses <= 10):

    guesses += 1

    a = int(input("Guess the number: "))
    
    if(a>n):
        print("Lower number please")
    elif (a == n):
        print(f"You have guessed the number {n} in {guesses} attempt")
        break
    else:
        print("Higher number please")
else:
    print(f"You did not find the right number {n}")

