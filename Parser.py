from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
import pickle
import json
import time



def get_html(url):
    file_news = []
    final_file_news = []
    now_time = datetime.datetime.today().strftime("%Y%m%d")
    file_news.append(now_time)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('a', {'class': 'content-feed__link'})

    for news in news_link:
        file_news.append(news.get('href'))


    return main_top(now_time, file_news)

def main_top(now, a):
    p = []
    c = [] #список для записи в файл
    k = []
    r = 0
    nf = open('news.txt', 'r+')
    print('Открыл файл')
    for line in nf.readlines():
        d = line.replace('\n', '')
        d = d.split(', ')

        if int(a[0]) - int(d[0]) < 5:
            print('Удаляем, строки с датами старше 3 дней')
            if a[0] == d[0]: # Сравниваем текущую дату и даты статей
                print('Обновляем ссылки на новости за сегодня')
                for j in c:  # Перебираем эленты списка С
                    k += j
                for i in a[1:]: # запускаем цикл проверки каждой полученной на текущий момент статьи
                    if i not in d: # Проверяем наличие статьи в текущей строке файлa
                        #if len(c) > 0: # Если список С не пустой то проверяем наличие полученных ссылок там
                        print('Метка записи2')

                        if i not in k: # Если ссылки нет в каких либо списках то добавляем ее в список по конкретной дате
                            d.append(i)
                            p.append(i)
                            r = 1 # Маркер того что дата новостей уже есть в списке и не нужно создавать новую строку
                            print('Метка записи1')
            c.append(d)

    if r == 0:
        d = []
        d.append(a[0])
        for m in c:
            k += m
        for i in a[1:]:
            if i not in k:
                d.append(i)
                p.append(i)
        c.append(d)
    nf.close()
    write_file(c)
    return p

def write_file(spis):
    if len(spis[-1]) > 1:
        nf = open('news.txt', 'w')
        for i in spis:
            r = 0
            for j in i:
                if len(i) - r == 1:
                    nf.write(j)
                else:
                    nf.write(j + ', ')
                    r += 1
            nf.write("\n")
        nf.close()
    return

#def run_bot(url):
   # while True:
   # m = get_html(url)
   # if m:
     #   print(m)
   # time.sleep(10)

#write_file('https://vc.ru/')
#print(get_html('https://vc.ru/'))