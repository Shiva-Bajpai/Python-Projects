import random

def math_quiz():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    
    print(f"What is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))
    
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")

math_quiz()
