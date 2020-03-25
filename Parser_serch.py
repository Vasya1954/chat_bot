from bs4 import BeautifulSoup
import requests

def get_html_serch(url):
    file_news = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('h3', {'class': 'entry-title td-module-title'})

    for link in news_link:
        file_news.append(link.find('a').get('href'))

    return file_news

def get_html_webmya(url):
    file_news = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('a', {'class': 'b-post_yablogs-major__title-link'})

    for news in news_link:
        file_news.append('https://webmaster.yandex.ru' + news.get('href'))

    return file_news

def get_html_cossa(url):
    file_news = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('a', {'class': 'article__title'})

    for news in news_link:
        file_news.append('https://www.cossa.ru' + news.get('href'))

    news_link = soup.find_all('a', {'class': 'new__content'})

    for news in news_link:
        file_news.append('https://www.cossa.ru' + news.get('href'))

    news_link = soup.find_all('div', {'class': 'article__title'})

    for link in news_link:
        file_news.append('https://www.cossa.ru' + link.find('a').get('href'))

    return file_news

def get_html_roem(url):
    file_news = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('header', {'class': 'news-block-article-header'})

    for link in news_link:
        file_news.append(link.find('a').get('href'))

    return file_news

def get_html_pixel(url):
    file_news = []


    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('div', {'class': 'block'})

    for link in news_link:
        link = str(link)
        if int(link[link.find('radius25">')+10:link.find('radius25">')+30][:link[link.find('radius25">')+10:link.find('radius25">')+30].rfind('</')][-4:]) >= 2020:
            file_news.append('https://tools.pixelplus.ru' + link[link.find('<a href="')+9:link.find('</a>')][:link[link.find('<a href="')+9:link.find('</a>')].rfind('">')])

    return file_news

def get_html_seonews(url):
    file_news = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers=headers)  # Получаем метод Response
    r.encoding = 'utf8'  # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('a', {'class': 'descr_link'})

    for news in news_link:
        file_news.append(news.get('href'))

    return file_news

def get_html_megaindex(url):
    file_news = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    news_link = soup.find_all('h2', {'class': 'topics-item__title'})

    for link in news_link:
        file_news.append('https://ru.megaindex.com' + link.find('a').get('href'))

    return file_news