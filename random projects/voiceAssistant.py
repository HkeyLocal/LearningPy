import speech_recognition as sr #Расшифровка голоса [pip install speech_recognition && pip install pyaudio]
import datetime # Использование времени [Предустановлен]
import pyttsx3 # Возспроизведение голоса [pip install pyttsx3]
import wikipedia # Поиск в википедии [pip install wikipedia]
import sys # Завершение программы [Предустановлен]
import webbrowser # Работа с браузером [Предустановлен]

username = 'Клим' # Имя пользователя 

def takeCMD(): # Функция получения голосовых команд
    r = sr.Recognizer() # Инициализация расшифратора 
    with sr.Microphone() as source:     # Использование микрофона
        audio_text = r.listen(source, timeout=0, phrase_time_limit=1) # переменная которая будет хранить записанный голос в течение phrase_time_limit
        try: # Защита от типа None в переменной audio_text
            command = r.recognize_google(audio_text, language='ru-RU') # Отправляем голос в сервис гугла для распознания голоса и указываем язык
            return command # Возвращаем команду в текстовом формате
        except:
            pass

def voice(query): # Функция воспроизведения голоса компьютера
    engine = pyttsx3.init()  # Инициализация движка
    voices = engine.getProperty('voices') # Получаем массив различных голосов
    engine.setProperty('voice', voices[2].id) # Выбираем голос для компьютера
    engine.say(query) # Инструмент воспроизведения запроса переданный в функцию
    engine.runAndWait() 
    
def minute(): # Функция для правильного произношения времени
    minutes = datetime.datetime.today().minute
    if minutes == 0:
        pass
    elif minutes == 1:
        return 'одна минута'
    elif minutes == 2:
        return 'две минуты'
    elif minutes == 3:
        return 'три минуты'   
    elif minutes == 4:
        return 'четыре минуты'
    else:
        return str(minutes) + 'минут'   
                
def Search(query): # Функция поиска в википедии
    wikipedia.set_lang('ru') # Устанавливаем язык поиска
    voice(wikipedia.summary(query, sentences=2)) # Воспроизводим ответ от википедии на наш запрос переданный в функцию

def Browser(query): # Функция для работы в браузере
    if 'открой браузер' in query: 
        webbrowser.open('https://www.google.ru')
    elif 'новости' in query:
        webbrowser.open('https://www.washingtonpost.com/')
    elif 'музыку' in query:    
        webbrowser.open('https://vk.com/audios336572376')
    elif 'в контакте' in query:
        webbrowser.open('https://vk.com/')
    else:
        if 'найди' in query:  # Удаление лишних слов для корректного запроса
            newquery = query.replace('найди', '')
        else:
            newquery = query.replace('выведи на экран', '')   
        webbrowser.open('https://www.google.ru/search?q={}'.format(newquery))

class Machine(object): # Объявляем класс Machine, который наследуется от object
    def __init__(self): # Инициализация главной функции
        while True: # Создаем фундамент для постоянного получения команд
            cmd = takeCMD() # Получение команды
            print('Идет запись команды') 
            if cmd != None: # Проверка на то, что кто-то вообще что-то сказал
                cmd = cmd.lower()   # Команду превращаем в команду с нижним регистром
                time = datetime.datetime.today() # Общая переменная для времени
                if 'время' in cmd: # Проверка по слову 
                    query = str(time.hour) + ' часов и ' + minute() # Вывод времени
                    voice(query) # Вызов функции для озвучки результата   
                elif 'найди' in cmd or 'поиск' in cmd: # Проверка по слову
                    query = cmd.replace('найди' or 'поиск', '') # Удаление лишних слов для корректного запроса
                    Search(query) # Вызов функции поиска в википедии
                elif 'спокойной ночи' in cmd or 'пока' in cmd: # Проверка по слову
                    voice('И вам спокойной ночи {}'.format(username)) # Вызов функции для озвучки результата   
                    sys.exit() # Закрытие программы
                elif 'открой' in cmd or 'найди' in cmd or 'выведи на экран' in cmd: # Проверка по слову
                    Browser(cmd) # Вызов функции браузера     
            else:
                print('Жду команды')

if __name__ == "__main__":    Machine() # Хороший тон               