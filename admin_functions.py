import json

import game

MENU = """
1. Add question
2. Remove question"""


def add_question(all_questions: list, questions_path: str = "questions.json"):
    try:
        new_question = input("Introdu o noua intrebare: ")
        possible_answers = input("Introdu toate raspunsurile posibilie separate prin ; ").split(";")
        for index, answer in enumerate(possible_answers):
            print(f"{index}. {answer}")

        correct_answer = int(input("Introdu una din cifre pentru raspunsul corect"))

        new_question_obj = {"question": new_question, "answers": possible_answers, "correctIndex": correct_answer}

        with open(questions_path, "w") as f:
            f.write(json.dumps({"questions": all_questions}, indent=4))

    except Exception as e:
        print("Error adding your question")



def delete_question():
    pass


def change_correct_answer(question):
    pass


def run():
    print(MENU)
    admin_pick = input("Alege o optiune: ")
    questions = game.read_questions()
    match admin_pick:
        case "1":
            add_question(questions)
        case "2":
            pass
        case _:   #cazul default
            exit(0)


if __name__ == '__main__':
    pass
