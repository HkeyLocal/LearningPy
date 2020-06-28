import random

class hangman(object):
    def listtoStr(list):
        prepare = ' '
        return(prepare.join(list))

    def __init__(self):
        self.number = random.randint(0, 1000)
        self.randword = open('wordlist.txt').read().split('\n')[self.number]
        self.length = len(self.randword)
        self.word = list(self.randword)
        success = list('*' * self.length)
        k = 0
        print('Загаданное слово - {}'.format(success) )
        print(self.randword)
        successindex = 0
        while k < 6:    
            i = 0
            answer = input('Введите букву ')
            while i < self.length:
                if answer == self.word[i]:
                    success[i] = answer
                    print('Вы угадали! {}'.format(hangman.listtoStr(success)))
                    successindex += 1
                    k = 0
                i += 1    
            k += 1
            if successindex == self.length:
                print('Ты выйграл! Твое слово: ', hangman.listtoStr(success))
                break        
        else:
            print('Вы проиграли!')     


hangman()