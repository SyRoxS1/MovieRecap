import mysql.connector



def check_if_movie_already_in_api(movie_id, letterbox_url):
    with open('password.txt', 'r') as file:
        password = file.read()
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        database='movies'
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM MoviesInfos WHERE name LIKE '{movie_id}' and ltrbx_url LIKE '{letterbox_url}'") 
    result = cursor.fetchall()

    if len(result) > 0:
        return True
    else:
        return False

check_if_movie_already_in_api("test", "test")