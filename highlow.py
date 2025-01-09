import random

def higher_or_lower():
    print("Higher or Lower Game!")
    number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
    else:
        print("Correct!")

higher_or_lower()
