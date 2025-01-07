def quiz_game():
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "Who wrote 'Hamlet'?": "shakespeare"
    }
    score = 0

    print("Welcome to the Quiz Game!")
    
    for question, correct_answer in questions.items():
        answer = input(f"{question} ").lower()
        if answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    print(f"You got {score}/{len(questions)} correct!")

quiz_game()
