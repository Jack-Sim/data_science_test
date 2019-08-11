# this is an attempt at web scrapping using the Beautiful Soup 4 package

# To install beautiful soup 4 run "pip3 install beautifulsoup4" in the command line

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

print(soup.title)
