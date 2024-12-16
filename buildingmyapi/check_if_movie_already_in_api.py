import mysql.connector



def check_if_movie_already_in_api(name, letterbox_url):
    with open('password.txt', 'r') as file:
        password = file.read()
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        database='movies'
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM MoviesInfos WHERE name LIKE '{name}' and ltrbx_url LIKE '{letterbox_url}'") 
    result = cursor.fetchall()

    if len(result) > 0:
        return True
    else:
        return False

