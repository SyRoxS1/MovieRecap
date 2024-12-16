from letterboxscarping import MovieDataProcessorLetter
import re
from bs4 import BeautifulSoup
from check_if_movie_already_in_api import check_if_movie_already_in_api




def getruntimeandName(data):
        NameWithRuntime = []
        soup = BeautifulSoup(data, 'html.parser')

        pattern = re.compile(r'runTime:\s*(\d+)')
        Name = re.search(r'name:\s*"([^"]+)"', data)
        extracted_name = Name.group(1) if Name else None
        match = pattern.search(data)

        runtime_value = match.group(1)
        NameWithRuntime.append([extracted_name, runtime_value])
        return NameWithRuntime
def getgenders(data):

        soup = BeautifulSoup(data, 'html.parser')

        jsondata = soup.find('script', {'type': 'application/ld+json'})
        jsondata = str(jsondata)

        pattern = re.compile(r'"genre":\s*\[([^\]]*)\]')
        match = pattern.search(jsondata)
        if match:
            genre_content = match.group(1)
            # Split the content into a list of genres
            genres = re.findall(r'"([^"]*)"', genre_content)
            return genres
        else:
            return "ERROR"

def getreleaseYear(data):
     # Define a regular expression pattern to match the releaseYear value
    pattern = r'var filmData = {.*?releaseYear: "(.*?)",'

    # Search for the pattern in the HTML code
    match = re.search(pattern, data, re.DOTALL)

    # Check if a match is found
    if match:
        release_year = match.group(1)
        return release_year
    else:
        print("Release Year not found in the HTML code.")
    with open("film_urls.txt","r") as f:
          toutlesfilms = f.readlines()

def Get_Text(film):
    Processor = MovieDataProcessorLetter
    fullurl = "https://letterboxd.com" + film
    text = Processor.EasyGetData(self="",Url=fullurl)
    return text


with open("film_urls.txt","r") as f:
      toutlesfilms = f.readlines()
count = 0

for film in toutlesfilms:
        Processor = MovieDataProcessorLetter
        count += 1

        film_clean = film.replace('\n','')

        text = Get_Text(film_clean)

        runtime_and_name = getruntimeandName(text)
        genders = getgenders(text)
        releaseyear = getreleaseYear(text)
        director =  str(Processor.getdirector(self="",data=text)).replace('[','').replace(']','').replace('\'','')
        print("Film number:", count)
        print("Film name:", runtime_and_name[0][0])
        print("Runtime:", runtime_and_name[0][1])
        print("Release year:", releaseyear)
        print('director:',director)

