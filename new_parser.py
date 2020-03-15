from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
import pickle
import json
import time



def get_html(url):
    file_news = []


    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('a', {'class': 'content-feed__link'})

    for news in news_link:
        file_news.append(news.get('href'))


    return main_top(file_news)

def main_top(file_news):
    print_list = []

    nf = open('news.txt', 'r+')
    line = nf.readline()
    list_line = line.split(', ')  # превращаем строку в список

    for link in file_news: #перебираем элементы новых url
        if link == list_line[0]:
            break
        print_list.append(link)

    list_line[0] = file_news[0]
    nf.close()
    write_file(list_line, print_list)

    return print_list

def write_file(list_line, print_list):
    nf = open('news.txt', 'w')
    r = 0
    for i in list_line:
        if len(list_line) - r == 1:
            nf.write(i)
        else:
            nf.write(i + ', ')
            r += 1
    nf.close()



while True:
    m = get_html('https://vc.ru/')
    if m:
        print(m)
    time.sleep(10)