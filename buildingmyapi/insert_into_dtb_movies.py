import mysql.connector



def insert_into_dtb_movies(name, runtime, genre,release_year, scenarist,letterbox_url):
    with open('password.txt', 'r') as file:
        password = file.read()
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        database='movies'
    )
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO MoviesInfos (name, length_minutes, genre, release_year, scenarist, ltrbx_url) VALUES ('{name}',{runtime},'{genre}',{release_year},'{scenarist}','{letterbox_url}')") 
    except:
        print("ERROR : can't execute:",f"INSERT INTO MoviesInfos (name, length_minutes, genre, release_year, scenarist, ltrbx_url) VALUES ('{name}',{runtime},'{genre}',{release_year},'{scenarist}','{letterbox_url}')")
    

    try:
        connection.commit()
    except:
        print("Can't commit...")
    cursor.close()  

    



