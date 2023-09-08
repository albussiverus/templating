

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pprint

url = 'https://en.wikipedia.org/wiki/Salo_(food)'
url_rozetka = 'https://rozetka.com.ua'

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')


my_tags = set()


for tag in bs.find_all(re.compile(".*")):
	my_tags.add(tag.name)

print((my_tags))

input()

# ссылки
set_links = set()
for link in bs.find_all(re.compile("^a")):
    set_links.add(link)

pprint.pprint(set_links)


for link in set_links:
	print(link.get_text())
