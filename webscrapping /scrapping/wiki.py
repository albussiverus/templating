from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Salo_(food)'
url_rozetka = 'https://rozetka.com.ua'


html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
