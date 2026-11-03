import random
def how_many_question():
    return int(input("How many math questions " \
    "would you like to be quized on: "))


def make_questions():
    operators = ["+", "-"]

    total_questions = how_many_question()
    question_to_save = []

    for i in range(total_questions):
        # 1. Pick two random numbers (e.g., between 1 and 20)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        # prevent negative subtractions
        if num2 > num1:
            temNum = num1
            num1 = num2
            num2 = temNum

        # 2. Randomly choose either "+" or "-"
        op = random.choice(operators)
        if op == "+":
            answer = num1 + num2
        elif op == "-":
            answer = num1 - num2

        line = f"{num1} {op} {num2}, {answer}\n"
        question_to_save.append(line)

        with open("questions.txt", "w") as file:
            file.writelines(question_to_save)



def main():
    make_questions()

main()
