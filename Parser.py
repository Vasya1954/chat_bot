from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
import pickle
import json
import time
import Parser_serch



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

    file_news += Parser_serch.get_html_serch('https://www.searchengines.ru/')
    file_news += Parser_serch.get_html_webmya('https://webmaster.yandex.ru/blog/')
    file_news += Parser_serch.get_html_cossa('https://www.cossa.ru/')
    file_news += Parser_serch.get_html_roem('https://roem.ru/')
    file_news += Parser_serch.get_html_pixel('https://tools.pixelplus.ru/news/')
    file_news += Parser_serch.get_html_seonews('https://www.seonews.ru/events/')
    file_news += Parser_serch.get_html_seonews('https://www.seonews.ru/analytics/')
    #file_news += Parser_serch.get_html_seonews('https://ru.megaindex.com/blog/')

    return check_url(file_news)

def write_url(url):
    with open('news.txt', 'a') as nf:
        new_list = [int(time.time()), check_h1(url), url]
        r = 0
        for i in new_list:
            if 3 - r == 1:
                nf.write(str(i))
            else:
                nf.write(str(i) + '; ')
                r += 1
        nf.write('\n')
    return

def url_open_file():
    with open('news.txt', 'r') as nf:
        url_list = []
        for line in nf.readlines():
            d = line.replace('\n', '')
            d = d.split('; ')
            url_list.append(d[2])

    return url_list

def check_url(a):
    for url in a:
        if url not in url_open_file():
            if url.find('vc.ru') != -1: #проверка похожих УРЛ на ВС
                m = ''
                for i in url_open_file():
                    m += i
                if url[url.rfind('/')+1:url.rfind('/')+7] not in m:
                    write_url(url)
            else:
                write_url(url)
    return

def check_h1(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers=headers)  # Получаем метод Response
    r.encoding = 'utf8'  # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    h1_title = str(soup.find('h1'))
    k = h1_title.find('>')
    l = h1_title.find('<', 2)

    if h1_title[k+1:l].strip() == 'Non':
        send = 'Новость без заголовка'
        return send
    else:
        return h1_title[k+1:l].strip()

def url_open_main():
    with open('news.txt', 'r') as nf:
        url_list = []
        for line in nf.readlines():
            d = line.replace('\n', '')
            d = d.split('; ')
            url_list.append(d)
    return url_list

