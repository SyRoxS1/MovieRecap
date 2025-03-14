import requests
from bs4 import BeautifulSoup
import re
import csv
from collections import Counter
import time
import datetime
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
            last_year = (int(datetime.datetime.now().year)) - 1
            with open(path, mode="r", encoding="utf8") as OpenFile:
                FileContent = csv.reader(OpenFile)
                next(FileContent)  # Supprime la première ligne car pas de films présents dessus
                
                for row in FileContent:
                    print(row[7][:4])
                    if row[7][:4] == str(last_year): #only get data from movies watched in 2023
                        self.Movies.append(row[1])
                        self.ReleaseDates.append(row[2])
                        self.letterboxdURI.append(row[3])

    def ReturnAllMovieLetterbox(self):
        return self.Movies
    
    def ReturnAllReleasesLetterbox(self):
        return self.ReleaseDates
    
    def ReturnAllURILetterbox(self):
        return self.letterboxdURI
    
    # Outdated
    """
    def GetDataFromMyAPI(self, MovieName): #GET DATA FROM MY API at https://movieapi.syroxs.online
        url= "https://movieapi.syroxs.online/" + MovieName
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            try:
                r = requests.get(url)
                data = r.text
                return data
            except:
                time.sleep(0.1)
                attempts += 1
        return('ERROR')

"""
    def GetDataFromAPI(self, MovieName):
        url = "https://api.themoviedb.org/3/search/movie?query="+MovieName+"&include_adult=false&language=en-US&page=1&year=1993"

        with open("auth.key","r") as file:
            key = file.readlines()

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {key}"
    }
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            try:
                r = requests.get(url, headers=headers)
                data = r.text
                return data
            except:
                time.sleep(0.1)
                attempts += 1
        return('ERROR FETCHING API for movie',MovieName)
    
    def getdirector(self, data):
        soup = BeautifulSoup(data, 'html.parser')

        jsondata = soup.find('script', {'type': 'application/ld+json'})
        jsondata = str(jsondata)

        pattern = re.compile(r'"director":\s*\[([^\]]*)\]')
        match = pattern.search(jsondata)
        director_name = []
        if match:
            director_content = match.group(1)
            # Split the content into a list of genres
            Name = re.search(r'name:\s*"([^"]+)"', data)
            extracted_name = Name.group(1) if Name else None
            director_name.append(extracted_name)
            
            director_name.append(re.findall(r'"name":\s*"([^"]*)"', director_content))

            
            return director_name
        else:
            return "ERROR"
        
    def StatGENDER(self, Genres): #Return percentgenders with all genders with the percentage of how much it is present in the whole list
        
        
        AllDifferentGenders = set(Genres)
        
        PercentGenders = {}

        for Gender in AllDifferentGenders:
            val = round(Genres.count(Gender)/len(Genres)*100,2)
            PercentGenders.update({Gender: val})
        return PercentGenders
    
    def TopGenders(self, PercentGenders):
        count = 0
        Top = []
        for Data in sorted(PercentGenders, key=PercentGenders.get, reverse=True):
            Top.append((Data, PercentGenders[Data]))
            count += 1
            if count == 3:
                break
        return Top
    
    def TopDirectors(self, Directors):
        Top = {}
        director_counts = Counter(Directors)

        # Step 2: Calculate the percentage of each director's appearances
        total_directors = len(Directors)
        director_percentages = {director: (count / total_directors) * 100 for director, count in director_counts.items()}

        # Step 3: Create a dictionary with director names as keys and their percentage as values
        director_percentage_dict = dict(sorted(director_percentages.items(), key=lambda x: x[1], reverse=True))

        # Step 4: Sort the dictionary based on the percentage in descending order
        sorted_director_percentage_dict = dict(sorted(director_percentage_dict.items(), key=lambda x: x[1], reverse=True))

        # Print the result
        for director, percentage in sorted_director_percentage_dict.items():
            Top.update({director: percentage})
        return Top
    
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