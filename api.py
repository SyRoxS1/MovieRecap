from flask import Flask, request, render_template
from main import AllTime, LongestWatch, StatGENDER, TopDirectors, TopGenders, topReleaseDate,MostWatchedDirector,ReleaseDateStats, NbFilmVu, MoviesF, RuntimeF




app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    Movies = MoviesF()
    Runtime = RuntimeF()
    TotalWatchTime = AllTime() #Renvoie temps en heures
    LongestWatchedTime = LongestWatch()
    LongestWatchedMovie = Movies[Runtime.index(str(LongestWatchedTime))]
    DataGenders = StatGENDER()
    Top3Directors = TopDirectors(MostWatchedDirector())
    Top3Genders = TopGenders(StatGENDER())
    topReleaseDateData = topReleaseDate(ReleaseDateStats())
    Nbfilms = NbFilmVu()
    
    return render_template('index.html',DATA=Nbfilms,)



if __name__ == '__main__':
    app.run("127.0.0.1", debug=True,port=4444)