questions = [
    ("What are genes?", ["a) Thread-like structures in cells", "b) Fundamental units of heredity", "c) Alternate forms of a gene", "d) Genomic segments responsible for environment adaptation"], 'b'),
    # Add more questions here...
    # ...
    ("What is the purpose of this note?", ["a) To discuss the importance of random mutations", "b) To explore the effects of environmental factors on genetics", "c) To provide an overview of essential genetic concepts and terms", "d) To analyze the relationship between genetics and psychology"], 'c')
]

def run_quiz(questions):
    score = 0

    # Iterate through each question and its choices
    for question, choices, correct_choice in questions:
        print(f"Question: {question}")

        # Iterate through each choice for the current question
        for choice in choices:
            print(choice)

        user_choice = input("Enter your choice: ").strip().lower()

        # Check the user's answer
        if user_choice == correct_choice:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was {correct_choice}.\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    run_quiz(questions)
