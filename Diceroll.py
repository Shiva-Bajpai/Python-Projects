import random

def dice_roll():
    print("Dice Rolling Simulator")
    while True:
        input("Press Enter to roll the dice...")
        print(f"You rolled: {random.randint(1, 6)}")
        if input("Roll again? (yes/no): ").lower() != "yes":
            break

dice_roll()
