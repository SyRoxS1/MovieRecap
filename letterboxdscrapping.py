import requests
from bs4 import BeautifulSoup
import re
def getdata(urllocal):
    r = requests.get(urllocal)

    data = r.text

    soup = BeautifulSoup(data, 'html.parser')

    element_with_data_target_link = soup.find('div', {'data-target-link': True})

    if element_with_data_target_link:
        data_target_link_content = element_with_data_target_link['data-target-link']
    else:
        print('error')

    url = "https://letterboxd.com"+str(data_target_link_content)
    r2 = requests.get(url)

    data = r2.text

    return data

def getgenders(data):
    
    soup = BeautifulSoup(data, 'html.parser')
    genders = soup.find('script', {'type': 'application/ld+json'})

    genders = str(genders)
    pattern = re.compile(r'"genre":\s*\[([^\]]*)\]')
    match = pattern.search(genders)
    if match:
        genre_content = match.group(1)
        # Split the content into a list of genres
        genres = re.findall(r'"([^"]*)"', genre_content)
        return genres
    else:
        return "ERROR"


