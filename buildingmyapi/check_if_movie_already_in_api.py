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
    try:
        cursor.execute(f"SELECT * FROM MoviesInfos WHERE name LIKE '{name}' and ltrbx_url LIKE '{letterbox_url}'") 
    except:
        print("ERROR executing :",f"SELECT * FROM MoviesInfos WHERE name LIKE '{name}' and ltrbx_url LIKE '{letterbox_url}'")

    try:
        result = cursor.fetchall()
        if len(result) > 0:
            return True
        else:
            return False
    except:
        print("Can't fetch")
        return True
        

    

