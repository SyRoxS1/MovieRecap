from flask import Flask, request, render_template, session, redirect
from main import  MovieDataProcessor
from letterboxdscrapping import MovieDataProcessorLetter
from all_genders_letterbxd import MovieDataProcessorLetterboxdAll
import re
import os
import random
import secrets
import hashlib


def generate_random_md5():
    # Generate a random value
    random_value = secrets.token_bytes(16)  # 16 bytes for a 128-bit value

    # Calculate the MD5 hash
    md5_hash = hashlib.md5(random_value).hexdigest()

    return md5_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/',methods=['GET'])
def indexchoice():
    return render_template('choice.html')

@app.route('/imbdupload',methods=['GET'])
def imbdupload():
    return render_template('uploadimdb.html')

@app.route('/letterupload',methods=['GET'])
def letterupload():
    return render_template('uploadletter.html')

@app.route('/uploadfromletter',methods=['POST'])
def uploadletter():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    folder = generate_random_md5()
    filename = generate_random_md5()
    os.makedirs("files/"+folder)
    path = "files/" + folder + "/" + filename +".csv"
    session['session_user'] = path
    session['type'] = "letterboxd"
    file.save(path)
    

    return redirect("/letterboxd_load")

@app.route('/letterboxd_load',methods=['GET'])
def letterboxd0():
    if session.get('type', 'Default Value') != "letterboxd":
        return redirect('/')
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    
    DataAllProcessor = MovieDataProcessorLetterboxdAll()
    
    
    Datas = DataAllProcessor.scanAPI(path) #Retrieve data from my API (name, runtime, Genders,release date,)
    session['Datas'] = Datas
    
    
    return redirect("/letterboxd")

@app.route('/letterboxd',methods=['GET'])
def letterboxd1():
    if session.get('type', 'Default Value') != "letterboxd":
        return redirect('/')
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    
    DataProcessor = MovieDataProcessorLetter()
    DataProcessor.readCSV(path)
    AllMovies = DataProcessor.ReturnAllMovieLetterbox()
    NbFilms = len(AllMovies)
    return render_template('index_letter.html',DATA=NbFilms)

@app.route('/letterboxdnext.html',methods=['GET'])
def letterboxd2():
    if session.get('type', 'Default Value') != "letterboxd":
        return redirect('/')
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    

    
    Datas = session.get('Datas','Default Value')
    if Datas == 'Default Value':
        return redirect('/')
    
    
    names = []
    runtimes = []
    Genders = []
    Release_Years = []
    
    
    for i in range(len(Datas)):
        names.append(Datas[i][1])
        runtimes.append(int(Datas[i][2]))
        Genders.append(Datas[i][3])
        Release_Years.append(Datas[i][4].replace("\n",""))
    
    total_duration = sum(runtimes)
    total_duration = total_duration / 60
    total_duration = round(total_duration, 2)
    return render_template('index2_letter.html',DATA=str(total_duration) +"H")

@app.route('/letterboxdnext2.html',methods=['GET'])
def letterboxd3():
    if session.get('type', 'Default Value') != "letterboxd":
        return redirect('/')
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    
    Datas = session.get('Datas','Default Value')
    if Datas == 'Default Value':
        return redirect('/')
    
    
    names = []
    runtimes = []
    Genders = []
    Release_Years = []
    
    
    for i in range(len(Datas)):
        names.append(Datas[i][1])
        runtimes.append(int(Datas[i][2]))
        Genders.append(Datas[i][3])
        Release_Years.append(Datas[i][4].replace("\n",""))

    max_where = runtimes.index(max(runtimes))
    longest_movie = names[max_where] 

    return render_template('index3_letter.html',DATA=longest_movie)


@app.route('/letterboxdnext3.html',methods=['GET'])
def letterboxd4():
    if session.get('type', 'Default Value') != "letterboxd":
        return redirect('/')
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    
    Datas = session.get('Datas','Default Value')
    if Datas == 'Default Value':
        return redirect('/')
    
    
    names = []
    runtimes = []
    Genders = []
    Release_Years = []
    
    
    for i in range(len(Datas)):
        names.append(Datas[i][1])
        runtimes.append(int(Datas[i][2]))
        Genders.append(Datas[i][3])
        Release_Years.append(Datas[i][4].replace("\n",""))

    max_where = runtimes.index(max(runtimes))
    length_max = runtimes[max_where]

    return render_template('index4_letter.html',DATA=length_max)

@app.route('/uploadfromimdb',methods=['POST'])
def uploadimbd():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    folder = generate_random_md5()
    filename = generate_random_md5()
    os.makedirs("files/"+folder)
    path = "files/" + folder + "/" + filename +".csv"
    session['session_user'] = path
    session['type'] = "imdb"
    file.save(path)
    

    return redirect("/imdb")

@app.route('/imdb', methods=['GET'])
def index():
    if session.get('type', 'Default Value') != "imdb":
        return redirect('/')
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)
    movie_processor.topReleaseDateData = movie_processor.topReleaseDate(movie_processor.ReleaseDateStats())
    Nbfilms = movie_processor.NbFilmVu()

    return render_template('index.html',DATA=Nbfilms)
    

@app.route('/nextpage.html', methods=['GET'])
def index2():
    path = session.get('session_user', 'Default Value')
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)
    TotalWatchTime = movie_processor.AllTime() #Renvoie temps en heures
    
    return render_template('index2.html',DATA=str(TotalWatchTime) +"H")

@app.route('/nextpage1.html', methods=['GET'])
def index3():
    path = session.get('session_user', 'Default Value')
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)
    Movies = movie_processor.MoviesF()
    Runtime = movie_processor.RuntimeF()
    movie_processor.LongestWatchedTime = movie_processor.LongestWatch()
    movie_processor.LongestWatchedMovie = Movies[Runtime.index(str(movie_processor.LongestWatchedTime))]
    return render_template('index3.html',DATA=movie_processor.LongestWatchedMovie)

@app.route('/nextpage2.html', methods=['GET'])
def index4():
    path = session.get('session_user', 'Default Value')
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)
    movie_processor.LongestWatchedTime = movie_processor.LongestWatch()
    return render_template('index4.html',DATA=str(movie_processor.LongestWatchedTime) +" minutes !!")

@app.route('/nextpage3.html', methods=['GET'])
def index5():
    path = session.get('session_user', 'Default Value')
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)

    pattern = r"'(.*?)'"

    DataGenders = movie_processor.StatGENDER()
    Top3Genders = movie_processor.TopGenders(movie_processor.StatGENDER())
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

@app.route('/nextpage4.html', methods=['GET'])
def index6():
    path = session.get('session_user', 'Default Value')
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)
    pattern = r"'(.*?)'"

    Top3Directors = movie_processor.TopGenders(movie_processor.MostWatchedDirector())
    print(Top3Directors)

    Top1 = Top3Directors[0]
    Top1 = str(Top1)
    Top1 = Top1.replace("(","")
    Top1 = Top1.replace(")","")
    match = re.search(pattern, Top1)
    extracted_text = match.group(1)
    Top1Director = extracted_text
    PercentOfDirector1 = Top1[Top1.index(",") +1:]

    Top2 = Top3Directors[1]
    Top2 = str(Top2)
    Top2 = Top2.replace("(","")
    Top2 = Top2.replace(")","")
    match = re.search(pattern, Top2)
    extracted_text = match.group(1)
    Top2Director = extracted_text
    PercentOfDirector2 = Top2[Top2.index(",") +1:]

    Top3 = Top3Directors[2]
    Top3 = str(Top3)
    Top3 = Top3.replace("(","")
    Top3 = Top3.replace(")","")
    match = re.search(pattern, Top3)
    extracted_text = match.group(1)
    Top3Director = extracted_text
    PercentOfDirector3 = Top3[Top3.index(",") +1:]



    return render_template('index6.html',DATA1=Top1Director,DATA2 = PercentOfDirector1,DATA3=Top2Director,DATA4 = PercentOfDirector2,DATA5=Top3Director,DATA6 = PercentOfDirector3)

if __name__ == '__main__':
    app.run("127.0.0.1", debug=True,port=4444)