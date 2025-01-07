import random

def hangman():
    word_list = ["python", "javascript", "ruby", "java"]
    word = random.choice(word_list)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(" ".join(guessed_word))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            if "".join(guessed_word) == word:
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    else:
        print(f"You've lost! The word was: {word}")

hangman()
