import telebot
import time
import Parser

bot = telebot.TeleBot('1055347540:AAGqd81bZ9lLL4v6o-k_IjIDN2anEp-Jq38')

@bot.message_handler(commands=['start'])
def start_message(message):
    if str(message.chat.id) not in Parser.find_user_id():
        Parser.add_user_id(Parser.find_user_id(), str(message.chat.id))
        bot.send_message(message.chat.id, 'Вы подписались на рассылку новостей, чтобы отписаться введите команду /stop')


    if message.chat.id == 171776816:
        t_now = int(time.time())
        while True:
            Parser.get_html('https://vc.ru/')
            for new in Parser.url_open_main():
                if int(new[0]) > t_now:
                    for id in Parser.find_user_id():
                        bot.send_message(str(id), new[1] + '\n' + new[2])
            t_now = int(time.time())
            time.sleep(600)

@bot.message_handler(commands=['infoid'])
def start_message(message):
    if message.chat.id == 171776816:
        for id in Parser.find_user_id():
            bot.send_message('171776816', str(id))

@bot.message_handler(commands=['stop'])
def start_message(message):
    Parser.del_id(str(message.chat.id))
    bot.send_message(message.chat.id, 'Вы отписаны от рассылки новостей')


bot.polling(none_stop=True)  # запускаем бота
