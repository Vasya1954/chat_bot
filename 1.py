import telebot
import config  # Импорт config.py
import Parser
import time


bot = telebot.TeleBot(config.token)  # Передаём токен из файла config.py



def start_message(message):
    t_now = int(time.time())
    while True:
        Parser.get_html(message)
        for new in Parser.url_open_main():
            if int(new[0]) > t_now:
                print(new[1] + '\n' + new[2])
        t_now = int(time.time())
        #time.sleep(600)

try:
    with open('text.txt', 'r') as nr:
        print(2)

except FileNotFoundError:
    with open('text.txt', 'w') as nr:
        print(1)



