import random

def roll_dice():
    print("Rolling the dice...")
    print(f"You rolled a {random.randint(1, 6)}!")

while True:
    roll_dice()
    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        break
