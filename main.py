import re 
import csv
from collections import defaultdict

DateOfInsertInList = []
Rating = [] 
ReleaseDates = [] 
Genres = []
Runtime = [] 
Directors = []
Movies = []
count = 0
GenderToSearch = "Horror"

with open("WATCHLIST.csv", mode="r", encoding="utf8") as OpenFile:
    FileContent = csv.reader(OpenFile)
    next(FileContent)  # Supprime la première ligne car pas de films présents dessus
    
    for row in FileContent:
        if row[3][:4] == '2023': #only get data from movies watched in 2023
            Movies.append(row[5])
            Genres.append(row[11])
            DateOfInsertInList.append(row[3])
            Rating.append(row[8])
            ReleaseDates.append(row[13])
            Runtime.append(row[9])
            Directors.append(row[14])


def LongestWatch(): 
    Total = 0 
    Longest = 0
    for EnumerationOfTime in Runtime:
        Total = int(Total) + int(EnumerationOfTime)
        if int(EnumerationOfTime) > Longest:
            Longest = int(EnumerationOfTime) 
    TotalTimeAll = round((Total/60),1)
    return Longest
    
def AllTime():
    Total = 0 
    Longest = 0
    for EnumerationOfTime in Runtime:
        Total = int(Total) + int(EnumerationOfTime)
    TotalTimeAll = round((Total/60),1)
    return TotalTimeAll


def StatGENDER(): #Return percentgenders with all genders with the percentage of how much it is present in the whole list
    GenderSeparated = []
    for EnumerationOfGenres in Genres:
        GenderSeparated = GenderSeparated + EnumerationOfGenres.split(",")
    AllDifferentGenders = set(GenderSeparated)
    
    PercentGenders = {}

    for Gender in AllDifferentGenders:
        val = round(Genres.count(Gender)/len(Genres)*100,2)
        PercentGenders.update({Gender: val})
    return PercentGenders


def TopGenders(PercentGenders):
    count = 0
    Top = []
    for Data in sorted(PercentGenders, key=PercentGenders.get, reverse=True):
        Top.append((Data, PercentGenders[Data]))
        count += 1
        if count == 3:
            break
    return Top




def SearchGender():
    with open("WATCHLIST.csv", mode="r", encoding="utf8") as OpenFile:
        FileContent = csv.reader(OpenFile)
        next(FileContent)  # Supprime la première ligne car pas de films présents dessus
        count = 0
        for row in FileContent:
            if GenderToSearch in row[11]:
                print(row[5])
                count = count + 1
        print("Number of the movie type :", count)



def MostWatchedDirector():
    UniqueDirectors = set(Directors)
    PercentDirector = {}
    
    for Director in UniqueDirectors:
        val = round(Directors.count(Director)/len(Directors)*100,2)
        PercentDirector.update({Director: val})
    return PercentDirector
    



def TopDirectors(PercentDirector):
    count = 0
    Top = []
    for Data in sorted(PercentDirector, key=PercentDirector.get, reverse=True):
        Top.append((Data, PercentDirector[Data]))
        count += 1
        if count == 3:
            break
    return Top


def ReleaseDateStats():
    years = []
    yearWithData = {}
    for SingleRelease in ReleaseDates:
        years.append(SingleRelease[:4])

    singleYear = set(years)


    for Year in singleYear:
        yearWithData.update({Year: years.count(Year)})
        
    return yearWithData

def topReleaseDate(yearWithData):
    Top = []
    count = 0
    for Data in sorted(yearWithData, key=yearWithData.get, reverse=True):
        Top.append((Data, yearWithData[Data]))
        count += 1
        if count == 3:
            break
    return Top

def NbFilmVu():
    return len(Movies) # :D

def MoviesF():
    return Movies #kappa

def RuntimeF():
    return Runtime

TotalWatchTime = AllTime() #Renvoie temps en heures
LongestWatchedTime = LongestWatch()
LongestWatchedMovie = Movies[Runtime.index(str(LongestWatchedTime))]
DataGenders = StatGENDER()
Top3Directors = TopDirectors(MostWatchedDirector())
Top3Genders = TopGenders(StatGENDER())
topReleaseDateData = topReleaseDate(ReleaseDateStats())

print(TotalWatchTime)
print(LongestWatchedTime)
print(LongestWatchedMovie)
print(Top3Directors)
print(Top3Genders)
print(topReleaseDateData)