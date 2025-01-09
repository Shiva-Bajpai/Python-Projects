import random

def word_scramble():
    words = ["python", "java", "ruby", "javascript"]
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    
    print(f"Unscramble this word: {scrambled}")
    guess = input("Your guess: ").lower()
    
    if guess == word:
        print("Correct!")
    else:
        print(f"Wrong! The word was {word}.")

word_scramble()
