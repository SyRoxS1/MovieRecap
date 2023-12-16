import re 
import csv
from collections import defaultdict

DateOfInsertInList = []
Rating = [] #8
ReleaseDate = [] #13
Genres = []
Runtime = [] #9
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
            ReleaseDate.append(row[13])
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
    AllDifferentGenders = []
    for EnumerationOfGenres in Genres: 
        GenderSeparated = GenderSeparated + EnumerationOfGenres.split(",")
    AllDifferentGenders = set(GenderSeparated)
    
    for Genders in AllDifferentGenders:
        PercentGenders = {}
        PercentGenders[Genders] = round(GenderSeparated.count(Genders)/len(GenderSeparated)*100,2)
    return PercentGenders

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

        val = PercentDirector[Director] = round(Directors.count(Director)/len(Directors)*100,2)
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
#regler probleme None



    

TotalWatchTime = AllTime()
LongestWatchedTime = LongestWatch()
LongestWatchedMovie = Movies[Runtime.index(str(LongestWatchedTime))]
DataGenders = StatGENDER()
Top3Directors = TopDirectors(MostWatchedDirector())
