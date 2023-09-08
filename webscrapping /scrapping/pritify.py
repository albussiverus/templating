
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Salo_(food)'
url_rozetka = 'https://rozetka.com.ua'

html = urlopen(url_rozetka)
bs = BeautifulSoup(html, 'html.parser')

for tag in bs.find_all('a'):
    print(tag)

