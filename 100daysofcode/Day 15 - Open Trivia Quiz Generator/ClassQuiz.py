from data import open_question_bank_data
from quiz_brain import QuizBrain
from question_model import Question
from html import unescape
open_question_bank = []
for question in open_question_bank_data:
    open_question_bank.append(Question(unescape(question["question"]),question["correct_answer"]))
quiz_brain = QuizBrain(open_question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.check_answer(quiz_brain.next_question())
    print(f"Your current score is {quiz_brain.score}/{quiz_brain.question_number}.\n")
print("That was the last question!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}.")