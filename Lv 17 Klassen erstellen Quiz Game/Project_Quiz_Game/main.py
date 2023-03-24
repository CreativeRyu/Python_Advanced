from question_model import Question
from data import question_data
from quiz_controller import QuizController

# 3 # # Wie kann die question_bank nach den oben importierten Modulen erzeugt werden # # # #
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

# # # # Zugriff auf die einzelnen Komponenten der Objektliste # # # #
# print(question_bank[0].text)

# -> to quiz_controller

#-----------------------------------------------------------------------------

quiz = QuizController(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Sie haben das Quiz abgeschlossen Sir")
print(f"Ihr finaler Punktestand beträgt {quiz.score} von {quiz.question_number} Punkten.")

# für weitere Fragepools kann man auf Open Trivia DB gehen und sich Pools geerieren lassen