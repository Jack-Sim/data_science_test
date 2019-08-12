# this is an attempt at web scrapping using the Beautiful Soup 4 package

# To install beautiful soup 4 run "pip3 install beautifulsoup4" in the command line

import requests
from bs4 import BeautifulSoup

def create_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

# Find and print all unique links that are on a page

def find_unique_links(soup):
    unique_links = []

    for link in soup.find_all("a"):
        url = link.get("href")

        if url in unique_links:
            pass
        else:
            unique_links += [url]
            print(url)
    print("There are " + str(len(unique_links)) + " links on this page")
    return unique_links

def find_page_description(page_list, home_url):
    output = {}

    for page in page_list:
        url = home_url + str(page)
        page_soup = create_soup(url)
        all_paragraphs = page_soup.find_all("p")

        for paragraph in all_paragraphs:
            if len(paragraph.text) < 50:
                pass
            else:
                output[page] = paragraph.text
    return output

url = input("Enter the URl you want to scrap: ")
soup = create_soup(url)
unique_links = find_unique_links(soup)
text_output = find_page_text(unique_links, url)
print(text_output["catalogue/a-light-in-the-attic_1000/index.html"])
