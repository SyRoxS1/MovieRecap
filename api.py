from flask import Flask, request, render_template
from main import AllTime, LongestWatch, StatGENDER, TopDirectors, TopGenders, topReleaseDate,MostWatchedDirector,ReleaseDateStats, NbFilmVu, MoviesF, RuntimeF
import re



app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    Top3Directors = TopDirectors(MostWatchedDirector())
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

    pattern = r"'(.*?)'"

    DataGenders = StatGENDER()
    Top3Genders = TopGenders(StatGENDER())
    Top1 = Top3Genders[0]
    Top1 = str(Top1)
    Top1 = Top1.replace("(","")
    Top1 = Top1.replace(")","")
    match = re.search(pattern, Top1)
    extracted_text = match.group(1)
    Top1Gender = extracted_text
    PercentOfGender1 = Top1[Top1.index(",") +1:]



    Top2 = Top3Genders[1]
    Top2 = str(Top2)
    Top2 = Top2.replace("(","")
    Top2 = Top2.replace(")","")
    match = re.search(pattern, Top2)
    extracted_text = match.group(1)
    Top2Gender = extracted_text
    PercentOfGender2 = Top2[Top2.index(",") +1:]

    Top3 = Top3Genders[2]
    Top3 = str(Top3)
    Top3 = Top3.replace("(","")
    Top3 = Top3.replace(")","")
    match = re.search(pattern, Top3)
    extracted_text = match.group(1)
    Top3Gender = extracted_text
    PercentOfGender3 = Top3[Top3.index(",") +1:]

    
    return render_template('index5.html',DATA1=Top1Gender,DATA2 = PercentOfGender1,DATA3=Top2Gender,DATA4 = PercentOfGender2,DATA5=Top3Gender,DATA6 = PercentOfGender3)




if __name__ == '__main__':
    app.run("127.0.0.1", debug=True,port=4444)