# #  works on Windows
import urllib.request

with urllib.request.urlopen('http://pythonscrapping.com/pages/page.1.html') as \
        response:
    html = response.read()

print(html)

# not work for me on windows
# from urllib.request import urlopen
#
# html = urlopen('http://pythonscrapping.com/pages/page.1.html')
# print(html.read())