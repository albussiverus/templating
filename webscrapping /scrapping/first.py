from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://uk.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BB%D0%BE_(%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%BD%D1%8F)"

url_2 = "http://pythonscrapping.com/pages/page.1.html"


url_3 = "https://en.wikipedia.org/wiki/Salo_(food)"

html = urlopen(url_3)

bs = BeautifulSoup(html, 'html.parser')





print(bs.find_all('a'))


for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

