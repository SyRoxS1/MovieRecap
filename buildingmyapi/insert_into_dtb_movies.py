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
    cursor.execute(f"INSERT INTO MoviesInfos (name, length_minutes, genre, release_year, scenarist, ltrbx_url) VALUES ('{name}','{runtime}','{genre}','{release_year}','{scenarist}','{letterbox_url}')") 
    connection.commit()
    cursor.close()  

    



