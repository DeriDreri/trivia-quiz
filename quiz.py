import requests
import ast
import random


class Question:
    def __init__(self, questions, number):
        self.number = number
        self.ansNum = 1 + len(questions['incorrect_answers'])
        self.qQ = questions['question']
        self.answers = list()
        self.answers.append(questions['correct_answer'])
        for i in questions['incorrect_answers']:
            self.answers.append(i)
        self.questionOrder = [0, 1, 2, 3]

    def askQuestion(self):
        random.shuffle(self.questionOrder)
        print("Question " + (str)(self.number+1))
        print(self.qQ)
        for i in range (0,self.ansNum):
            print((str)(i+1) + ". " + self.answers[self.questionOrder[i]])

    def answerQuestion(self):
        answer = input("Answer? [1,2,3,4]:" )
        if(self.questionOrder[(int)(answer)-1] == 0):
            print("Correct answer!")
            return 1
        else:
            print("Incorrect answer!")
            print("Correct answer was: ")
            print(self.answers[0])
            return 0
            

def getQuestions(url):
    file = requests.get(url)
    text = file.text
    finalText = text[29:-1]
    array = ast.literal_eval(finalText)
    questions = list()
    for i in range (0, len(array)):
        questions.append(Question(array[i],i))
        
    return questions

def main():
    questions = getQuestions("https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple")
    points = 0
    for question in questions:
        question.askQuestion()
        points += question.answerQuestion()
    print("Your points: " + str(points))

if __name__ == "__main__":
    main()
