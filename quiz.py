import question_maker

def load_questions():
    questions = []

    with open("questions.txt", "r") as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                questions.append(parts)
    return questions

def run_quiz():
    questions = load_questions()
    if not questions:
        print("No questions found!")
        return

    score = 0
    questionNum = 0
    for q, a in questions:
        questionNum += 1
        print(f"\n{questionNum}) Question: {q}")
        user_answer = input("Enter your answer: ")

        if user_answer.strip().lower() == a.strip().lower():
            print("Correct Answer!")
            score += 1
        else:
            print("Incorrect Answer!")

    print(f"\nScore: {score}")

def main():
    run_quiz()
    input("Press Enter to Exit.")

if __name__ == "__main__":
    main()
