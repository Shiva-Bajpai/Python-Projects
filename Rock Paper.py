import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nType 'rock', 'paper', or 'scissors' to play.")
        print("Type 'quit' to end the game.")
        user_choice = input("Your choice: ").lower()
        
        if user_choice == "quit":
            print(f"\nFinal Scores - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

if __name__ == "__main__":
    rock_paper_scissors()
