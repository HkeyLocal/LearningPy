class rock_paper_scissors(object):
    def __init__(self):
        self.computerAns = random.randint(1,3) # 1 - Rock; 2 - Paper; 3 - Scissors
        print('Компьютер сделал выбор!')

    def checkAnswer():
        check = rock_paper_scissors()
        print('1 - Rock; 2 - Paper; 3 - Scissors')
        answer = int(input('Сделай свой выбор: '))
        if answer == 1:
            if check.computerAns == 1:
                print('Ничья')
            elif check.computerAns == 2:
                print('Ты проиграл')
            else:
                print('Ты выйграл')         
        if answer == 2:
            if check.computerAns == 1:
                print('Ты выйграл')
            elif check.computerAns == 2:
                print('Ничья')
            else:
                print('Ты проиграл')
        if answer == 3:
            if check.computerAns == 1:
                print('Ты проиграл')
            elif check.computerAns == 2:
                print('Ты выйграл')
            else:
                print('Ничья')    

rock_paper_scissors.checkAnswer();   
