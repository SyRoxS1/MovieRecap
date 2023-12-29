import re 
import csv
from collections import defaultdict

class MovieDataProcessor:
    def __init__(self):
        self.DateOfInsertInList = []
        self.Rating = [] 
        self.ReleaseDates = [] 
        self.Genres = []
        self.Runtime = [] 
        self.Directors = []
        self.Movies = []
        self.count = 0
        self.GenderToSearch = "Horror"

    def readCSV(self, path):
        with open(path, mode="r", encoding="utf8") as OpenFile:
            FileContent = csv.reader(OpenFile)
            next(FileContent)  # Supprime la première ligne car pas de films présents dessus

            for row in FileContent:
                if row[3][:4] == '2023': #only get data from movies watched in 2023
                    self.Movies.append(row[5])
                    self.Genres.append(row[11])
                    self.DateOfInsertInList.append(row[3])
                    self.Rating.append(row[8])
                    self.ReleaseDates.append(row[13])
                    self.Runtime.append(row[9])
                    self.Directors.append(row[14])
            

    def LongestWatch(self): 
        Total = 0 
        Longest = 0
        for EnumerationOfTime in self.Runtime:
            Total = int(Total) + int(EnumerationOfTime)
            if int(EnumerationOfTime) > Longest:
                Longest = int(EnumerationOfTime) 
        TotalTimeAll = round((Total/60),1)
        return Longest

    def AllTime(self):
        Total = 0   
        Longest = 0
        for EnumerationOfTime in self.Runtime:
            Total = int(Total) + int(EnumerationOfTime)
        TotalTimeAll = round((Total/60),1)
        return TotalTimeAll


    def StatGENDER(self): #Return percentgenders with all genders with the percentage of how much it is present in the whole list
        GenderSeparated = []
        for EnumerationOfGenres in self.Genres:
            GenderSeparated = GenderSeparated + EnumerationOfGenres.split(",")
        AllDifferentGenders = set(GenderSeparated)

        PercentGenders = {}

        for Gender in AllDifferentGenders:
            val = round(self.Genres.count(Gender)/len(self.Genres)*100,2)
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




    def SearchGender(self):
        with open("WATCHLIST.csv", mode="r", encoding="utf8") as OpenFile:
            FileContent = csv.reader(OpenFile)
            next(FileContent)  # Supprime la première ligne car pas de films présents dessus
            count = 0
            for row in FileContent:
                if self.GenderToSearch in row[11]:
                    print(row[5])
                    count = count + 1
            print("Number of the movie type :", count)



    def MostWatchedDirector(self):
        UniqueDirectors = set(self.Directors)
        PercentDirector = {}

        for Director in UniqueDirectors:
            val = round(self.Directors.count(Director)/len(self.Directors)*100,2)
            PercentDirector.update({Director: val})
        return PercentDirector




    def TopDirectors(self, PercentDirector):
        count = 0
        Top = []
        for Data in sorted(PercentDirector, key=PercentDirector.get, reverse=True):
            Top.append((Data, PercentDirector[Data]))
            count += 1
            if count == 3:
                break
        return Top


    def ReleaseDateStats(self):
        years = []
        yearWithData = {}
        for SingleRelease in self.ReleaseDates:
            years.append(SingleRelease[:4])

        singleYear = set(years)


        for Year in singleYear:
            yearWithData.update({Year: years.count(Year)})

        return yearWithData

    def topReleaseDate(self, yearWithData):
        Top = []
        count = 0
        for Data in sorted(yearWithData, key=yearWithData.get, reverse=True):
            Top.append((Data, yearWithData[Data]))
            count += 1
            if count == 3:
                break
        return Top

    def NbFilmVu(self):
        return len(self.Movies) # :D

    def MoviesF(self):
        return self.Movies #kappa

    def RuntimeF(self):
        return self.Runtime

