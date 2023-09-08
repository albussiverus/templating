from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h2
    except AttributeError:
        return None

    return title


if __name__ == "__main__":
    title_res = get_title('http://www.pythonscraping.com/pages/page1.html')
    if title_res is None:
        print('Title could not be found')
    else:
        print(title_res)
