class generatorPasswd(object):
    def __init__(self):
        while True:
            self.letters = ''
            self.numbers = ''
            self.length = int(input('Укажите длину пароля '))
            self.countLetters = int(input('Укажите количество букв в пароле '))
            self.countNumbers = int(input('Укажите количество цифр в пароле '))
            if self.length < self.countLetters + self.countNumbers:
                print('Сумма количества цифр и букв, больше длины пароля')
                continue
            else:
                break
        self.upperCase = int(input('Укажите 0, если вам не нужны большие буквы, 1 если нужны, 2 если хотите смешать большие и маленькие буквы '))
        if self.upperCase == 0:
            self.type = string.ascii_lowercase
        elif self.upperCase == 1:
            self.type = string.ascii_uppercase
        else:
            self.type = string.ascii_letters 
        i = 0    
        while i < self.countLetters:
            self.letters += random.choice(self.type)
            i += 1;
        else:
            i = 0;    
        while i < self.countNumbers:
            self.numbers += str(random.randint(0, 9))
            i += 1
        else:
            i = 0
    def main():
        generator = generatorPasswd()        
        prepared = generator.letters + generator.numbers
        ready = random.sample(prepared, generator.length)
        passwd = ' '
        answer = passwd.join(ready)
        return(answer.replace(' ', ''))

def passgen():
    question = int(input('Вы хотите сгенерировать пароль? 0 - нет, 1 - да '))
    password = generatorPasswd.main()
    print('Ваш пароль ', password)       
