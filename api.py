from flask import Flask, request, render_template
from main import AllTime, LongestWatch, StatGENDER, TopDirectors, TopGenders, topReleaseDate,MostWatchedDirector,ReleaseDateStats, NbFilmVu, MoviesF, RuntimeF




app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    
    
    DataGenders = StatGENDER()
    Top3Directors = TopDirectors(MostWatchedDirector())
    Top3Genders = TopGenders(StatGENDER())
    topReleaseDateData = topReleaseDate(ReleaseDateStats())
    Nbfilms = NbFilmVu()
    
    return render_template('index.html',DATA=Nbfilms,)

@app.route('/nextpage.html', methods=['GET'])
def index2():
    TotalWatchTime = AllTime() #Renvoie temps en heures
    return render_template('index2.html',DATA=str(TotalWatchTime) +"H")

@app.route('/nextpage1.html', methods=['GET'])
def index3():
    Movies = MoviesF()
    Runtime = RuntimeF()
    LongestWatchedTime = LongestWatch()
    LongestWatchedMovie = Movies[Runtime.index(str(LongestWatchedTime))]
    return render_template('index3.html',DATA=LongestWatchedMovie)

@app.route('/nextpage2.html', methods=['GET'])
def index4():
    LongestWatchedTime = LongestWatch()
    return render_template('index4.html',DATA=str(LongestWatchedTime) +" minutes !!")

@app.route('/nextpage3.html', methods=['GET'])
def index5():
    
    return render_template('index5.html',DATA=)




if __name__ == '__main__':
    app.run("127.0.0.1", debug=True,port=4444)