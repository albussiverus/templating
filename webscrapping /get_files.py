from bs4 import BeautifulSoup
import requests


url = "http://www.pythonscraping.com/pages/warandpeace.html"


def get_html(url):
    obj = requests.get(url)
    return obj.text

# "html.parser"
def handle_bs(obj_html):
    obj = get_html(url)
    bs = BeautifulSoup(obj, "html.parser")
    return bs




if __name__ == "__main__":
    print(handle_bs(url))
