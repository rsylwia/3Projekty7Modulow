import csv
import mysql.connector

with mysql.connector.connect(user='sql7613272', password='tx4wKLINir', host='sql7.freemysqlhosting.net',
                             database='sql7613272') as connection:
    cursor = connection.cursor()

    with open('city.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                previous_position = int(row['2021'])
            except:
                previous_position = 0
            sql = f"""INSERT INTO
                  city(name, country, position, previous_position)
                  VALUES('{row['City']}', '{row['Country']}', '{int(row['2022'])}', '{int(row['2021'])}')
                  """
            cursor.execute(sql)
        connection.commit()
