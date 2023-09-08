
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Salo_(food)'
# url_rozetka = 'https://rozetka.com.ua'

html = urlopen(url)
#print(html.read())
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
#
# for tag in bs.find_all(True):
#     print(tag.name)
#
# def has_class_but_no_id(mytag):
#     return mytag.has_attr('class') and not mytag.has_attr('id')
#
#
# for tag in bs.find_all(has_class_but_no_id):
#     print(f"this is a tag: {tag.name}")
