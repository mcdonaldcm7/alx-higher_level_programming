#!/usr/bin/python3
"""
This module uses the MySQLdb to connect to the database passed as argument and
prints all the cities of the 'hbtn_0e_4_usa' database.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)

    cur = conn.cursor()
    sql_query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
