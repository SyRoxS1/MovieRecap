from flask import Flask, request, render_template, session, redirect
from main import  MovieDataProcessor
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
def test():
    return render_template('uploadimdb.html')

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
    file.save(path)
    

    return redirect("/imdb")

@app.route('/imdb', methods=['GET'])
def index():
    
    path = session.get('session_user', 'Default Value')
    if path == "Default Value":
        return redirect('/')
    
    movie_processor = MovieDataProcessor()
    movie_processor.readCSV(path)
    movie_processor.topReleaseDateData = movie_processor.topReleaseDate(movie_processor.ReleaseDateStats())
    Nbfilms = movie_processor.NbFilmVu()

    return render_template('index.html',DATA=Nbfilms,)
    

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