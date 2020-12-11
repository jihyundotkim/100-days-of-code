class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        self.question_number += 1
        return user_answer
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number-1].answer.lower():
            print("You got it!")
            self.score +=1;
        else:
            print("That's incorrect.")
        print(f"The correct answer is {self.question_list[self.question_number-1].answer}")
        