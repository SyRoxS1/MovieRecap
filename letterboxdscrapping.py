import requests
from bs4 import BeautifulSoup
import re

def getgenders(urllocal):
    r = requests.get(urllocal)




    data = r.text

    soup = BeautifulSoup(data, 'html.parser')


    element_with_data_target_link = soup.find('div', {'data-target-link': True})


    if element_with_data_target_link:
        data_target_link_content = element_with_data_target_link['data-target-link']
        print("Content inside data-target-link:", data_target_link_content)
    else:
        print("Element with data-target-link attribute not found.")

    url = "https://letterboxd.com"+str(data_target_link_content)
    print("url: " + url)
    r2 = requests.get(url)

    data = r2.text
    print(len(r2.text))
    soup = BeautifulSoup(data, 'html.parser')
    genders = soup.find('script', {'type': 'application/ld+json'})

    genders = str(genders)
    pattern = re.compile(r'"genre":\s*\[([^\]]*)\]')
    match = pattern.search(genders)
    if match:
        genre_content = match.group(1)
        # Split the content into a list of genres
        genres = re.findall(r'"([^"]*)"', genre_content)
        print("Movie genres:", genres)
    else:
        print("dommage")

