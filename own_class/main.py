from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    question = Question(question_data[i]["text"], question_data[i]["answer"] )
    question = question_bank.append()


print(question_bank)