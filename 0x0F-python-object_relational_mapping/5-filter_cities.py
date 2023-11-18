#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect database using the command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    # create the cursor object to iterate with database
    my_cursor = my_db.cursor()

    # exercuting the SELECT quary to fatch the data
    my_cursor.execute(
        """SELECT * FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id""")

    print(", ".join([city[2]
                     for city in my_cursor.fetchall()
                     if city[4] == argv[4]]))

    # closing all the cursor
    my_cursor.close()

    # closing all the database
    my_db.close
