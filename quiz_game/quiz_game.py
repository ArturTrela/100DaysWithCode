class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.user_choice = ""
        self.condition = True

    def still_has_questions(self, ):
        return self.question_number < len(self.question_list)

    def check_answer(self):

        q_answer = self.question_list[self.question_number - 1]
        if self.user_choice == q_answer.answer and len(self.question_list) < 13:
            self.score += 1
            print(f'Right ! Your actual score is {self.score} / {self.question_number}')
        else:
            print(f'Wrong !')
            if self.question_number == len(self.question_list):
                print(f'Your TOTAL  score is {self.score} / {self.question_number}')
            else:
                print(f'Your actual  score is {self.score} / {self.question_number}')

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        print("\n")
        self.user_choice = input(f'Q.{self.question_number}: {question.text} (True / False) ? ').capitalize()
        return self.user_choice
