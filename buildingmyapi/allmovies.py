from bs4 import BeautifulSoup
import re
import requests
"""
gather all movies from a letterboxd list wich contains 20k movies (then added to a database for my api)
"""
#with open("allmoveis.txt","r") as f:
#    urls = f.readlines()

def readhhtml(html):
    print("parsing : " + html)
    soup = BeautifulSoup(html, 'html.parser')

    film_urls = []

    # Find all <div> elements with class "poster" and extract the 'data-target-link' attribute
    poster_divs = soup.find_all('div', class_='poster')
    for div in poster_divs:
        target_link = div.get('data-target-link')
        if target_link:
            film_urls.append(target_link)

    # Output the extracted URLs
    with open('film_urls.txt', 'a') as file:
        for url in film_urls:
            file.write(url + '\n')
    return

def gethtml(url):
    r = requests.get(url)
    html = r.text  
    return html



url = "https://letterboxd.com/annwilson50/list/all-movies/"
html = gethtml(url)
readhhtml(html)
