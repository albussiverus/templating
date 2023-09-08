from bs4 import BeautifulSoup as mybs
import requests

from urllib.request import urlopen


def html_data(url: str):
    soup = None
    try:
        page = requests.get(url)
        soup = mybs(page.text, 'html')
        # print(soup.prettify())
    except requests.exceptions.ConnectionError as e:
        print(e)

    return soup

def html_data_uo(url):
    soup = None
    try:
        page = urlopen(url)
        soup = mybs(page.read(), 'html.parser')
        # print(soup.prettify())
    except requests.exceptions.ConnectionError as e:
        print(e)

    return soup

if __name__ == "__main__":
    url = 'http://www.pythonscraping.com/pages/warandpeace.html'

    url_w =  'https://en.wikipedia.org/wiki/Salo_(food)'
    ur_forms = "http://www.pythonscraping.com/pages/form.html"


    # txt = html_data(url_w)
    # print(txt)

    txt_2 = html_data_uo(url_w)
    print(txt_2)
