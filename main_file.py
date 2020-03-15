import telebot
from telebot import apihelper  # Нужно для работы Proxy
import config  # Импорт config.py
import urllib.request  # request нужен для загрузки файлов от пользователя
import socket
import socks
import Parser

ip = '128.140.175.99'  # change your proxy's ip
port = 443   # change your proxy's port
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
#socket.socket = socks.socksocket

bot = telebot.TeleBot(config.token)  # Передаём токен из файла config.py


@bot.message_handler(commands=['start'])
def start_message(message):
    for new in Parser.get_html('https://vc.ru/'):
        bot.send_message(message.chat.id, new)


bot.polling(none_stop=True, timeout=123)  # запускаем бота
