from bs4 import BeautifulSoup
import requests

with open('urls.txt', 'r') as nf:
    url_list = []
    for line in nf.readlines():
        d = line.replace('\n', '')
        url_list.append(d)

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

for url in url_list:

    r = requests.get(url, headers = headers)    # Получаем метод Response
    r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
    soup = BeautifulSoup(r.text, 'html.parser')
    #m = soup.find('a', {'class': '_13ptbeu'}).get('href')
    d = soup.find('div', {'class': 'b-doctor-stats__stats-num'}).text
    m = soup.find('div', {'class': 'b-doctor-details__toc-num'}).text
    print(url, d, m)


