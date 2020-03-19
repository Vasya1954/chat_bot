import time
import requests
from bs4 import BeautifulSoup

a = ['https://www.cossa.ru/news/260314/', 'https://vc.ru/books/113620-rasprostranenie-infekcii-zhivotnyh-i-sleduyushchaya-chelovecheskaya-pandemiya-glavnye-idei-knigi-devida-kvammena', 'https://vc.ru/media/113471-verstka-stati-v-the-new-york-times-o-samoizolyacii-vo-vremya-pandemii-covid-19']

def write_url(url):
    with open('news.txt', 'a') as nf:
        new_list = [int(time.time()), check_h1(url), url]
        r = 0
        for i in new_list:
            if 3 - r == 1:
                nf.write(str(i))
            else:
                nf.write(str(i) + ', ')
                r += 1
        nf.write('\n')
    return

def url_open_file():
    with open('news.txt', 'r') as nf:
        url_list = []
        for line in nf.readlines():
            d = line.replace('\n', '')
            d = d.split(', ')
            url_list.append(d[2])

    return url_list

def check_url(a):
    for url in a:
        if url not in url_open_file():
            write_url(url)

def check_h1(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers=headers)  # Получаем метод Response
    r.encoding = 'utf8'  # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    h1_title = str(soup.find('h1'))
    k = h1_title.find('>')
    l = h1_title.rfind('<')

    return h1_title[k+1:l].strip()


check_url(a)
#print(write_url('https://vc.ru/tribuna/86111-apix-drive-onlayn-konnektor-raznyh-servisov-i-prilozheniy-mezhdu-soboy-bez-programmistov'))



