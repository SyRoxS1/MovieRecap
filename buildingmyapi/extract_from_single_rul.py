from letterboxscarping import MovieDataProcessorLetter
import re
from bs4 import BeautifulSoup


with open("film_urls.txt","r") as f:
      toutlesfilms = f.readlines()


def getruntime(data):
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

def jsp(film):
    Processor = MovieDataProcessorLetter
    fullurl = "https://letterboxd.com" + film
    text = Processor.EasyGetData(self="",Url=fullurl)
    return text

count = 0
for film in toutlesfilms:
      Processor = MovieDataProcessorLetter
      count += 1

      filmoui = film.replace('\n','')

      text = jsp(filmoui)

      lesdatas = getruntime(text)
      lesdatas2 = getgenders(text)
      releaseyear = getreleaseYear(text)
      director =  Processor.getdirector(self="",data=text)
      with open('movies_length.txt', 'a') as file:
        file.write(' '.join(map(str, lesdatas)) + "," +' '.join(map(str, lesdatas2)) + ","+ releaseyear +","+ str(director) + "\n")