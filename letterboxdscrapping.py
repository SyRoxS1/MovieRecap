import requests
from bs4 import BeautifulSoup
import re
import csv
"""
Most of the function here are now useless :
getdata() used to redirect the uri url from the csv (cf letterboxd csv) to the actual website page
getgenders() wich gather the genders from some javascript code that was on the website is now useless since my API sends it (faster)
getruntime() same as getgenders()
getdirector() i may have forgotten to add the director to my API...
"""

class MovieDataProcessorLetter:
    def __init__(self):
        self.DateOfInsertInList = []
        self.ReleaseDates = [] 
        self.Genres = []
        self.Runtime = [] 
        self.Directors = []
        self.Movies = []
        self.letterboxdURI = []
        self.count = 0
        
        

    def readCSV(self, path):
            with open(path, mode="r", encoding="utf8") as OpenFile:
                FileContent = csv.reader(OpenFile)
                next(FileContent)  # Supprime la première ligne car pas de films présents dessus
                
                for row in FileContent:
                    if row[7][:4] == '2023': #only get data from movies watched in 2023
                        self.Movies.append(row[1])
                        self.ReleaseDates.append(row[2])
                        self.letterboxdURI.append(row[3])

    def ReturnAllMovieLetterbox(self):
        return self.Movies
    
    
    
    def ReturnAllURILetterbox(self):
        return self.letterboxdURI
    
    def GetDataFromMyAPI(self, MovieName): #GET DATA FROM MY API at https://movieapi.syroxs.online
        url= "https://movieapi.syroxs.online/" + MovieName
        r = requests.get(url)
        data = r.text
        return data
    
    
    
    def getdirector(self, data):
        soup = BeautifulSoup(data, 'html.parser')

        jsondata = soup.find('script', {'type': 'application/ld+json'})
        jsondata = str(jsondata)

        pattern = re.compile(r'"director":\s*\[([^\]]*)\]')
        match = pattern.search(jsondata)
        if match:
            director_content = match.group(1)
            # Split the content into a list of genres
            director = re.findall(r'"([^"]*)"', director_content)
            director_name = re.findall(r'"name":\s*"([^"]*)"', director_content)
            return director_name
        else:
            return "ERROR"
    """
    def getgenders(self, data):

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
    """
    """
    def getdata(self, urllocal): #NOT USEFULL ANYMORE give a uri and respond with the text of the actual url of the movie (https://boxd.it/55bA6B -> https://letterboxd.com/film/godzilla-2014/)
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
    """
    
    """
    def getruntime(self, data):
        self.NameWithRuntime = []
        soup = BeautifulSoup(data, 'html.parser')

        pattern = re.compile(r'runTime:\s*(\d+)')
        Name = re.search(r'name:\s*"([^"]+)"', data)
        extracted_name = Name.group(1) if Name else None
        match = pattern.search(data)
        
        runtime_value = match.group(1)
        self.NameWithRuntime.append([extracted_name, runtime_value])
        return self.NameWithRuntime

    """