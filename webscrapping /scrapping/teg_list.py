
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pprint

url = 'https://en.wikipedia.org/wiki/Salo_(food)'
url_rozetka = 'https://rozetka.com.ua'

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')


# my_tags = set()
# for tag in bs.find_all(re.compile(".*")):
#     my_tags.add(tag.name)
# #
# print(my_tags)

# input()

# store = list()
# for tag in bs.find_all(['a', 'div']):
#     store.append(tag)
# print(store)


# #
# input()
# pprint.pprint(store)
#
# print("*"*20)
# print(bs)
# for tag in bs.find_all('button', attrs={'title': 'Visa Verified'}):
#     print(tag)

for tag in bs.find_all('div', attrs={'id': 'bodyContent'}):
    print(tag)
