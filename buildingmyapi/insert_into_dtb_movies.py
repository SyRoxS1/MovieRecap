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
    cursor.execute(f"") 
    result = cursor.fetchall()

    if len(result) > 0:
        return True
    else:
        return False

