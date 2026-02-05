# game.py
from questions import questions

def start_game():
    score = 0
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ")
        if answer.lower() == q["answer"].lower():
            score += 1
            print("Correct!\n")
        else:
            print("Wrong!\n")

    print(f"Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    start_game()
