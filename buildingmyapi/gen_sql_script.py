import ast

def generate_sql_script(movie_data):
    # Create table statement
    # (Assuming the table 'movies' already exists)

    # Insert data statements
    insert_sql = 'INSERT INTO MoviesInfos (name, length_minutes, genre, release_year) VALUES'

    # Prepare values for each row
    values_list = []
    
    values = "('{}', {}, '{}', {})".format(data[0], data[1], data[2], data[3])
    values_list.append(values)

    # Join values for all rows
    values_sql = ',\n'.join(values_list)

    # Combine statements
    full_sql_script = f'{insert_sql}\n{values_sql};'

    return full_sql_script

with open('D:/leo from old pc/programmation/python/MovieRecap/buildingmyapi/movies_length.txt', 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        data = line
        data = data.replace("[","")
        data = data.replace("]","")
        data = data.replace("'","")
        data = data.replace("\\","")
        
        
        test = data.split(",")
        if len(test) == 5:
            data = data.replace(",","",1)
        if len(test) == 6:
            data = data.replace(",","",2)
        if len(test) == 7:
            data = data.replace(",","",3)


        data = data.split(",")
        script = generate_sql_script(data)
        with open("script2_sql.sql",'a', encoding='utf-8') as file2:
            print(script)
            file2.write(script + "\n")
        
        
