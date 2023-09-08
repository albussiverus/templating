import urllib.request as req

url = "http://pythonscrapping.com/pages/page.1.html"

with req.urlopen(url) as responce:
    html = responce.read()

print(html)
