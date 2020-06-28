import random

class whatNumber():
    def __init__(self):
        self.number = random.randint(0, 20)
        print('Инициализировано число')

    def checkAnswer():
        answer = input('Предположи число ')
        rand = whatNumber()
        succes = rand.number
        if str(answer) == succes:
            print(succes)
            print('You are right!')
        else: 
            print('Your answer is wrong!')
            print(succes)
            
whatNumber.checkAnswer()