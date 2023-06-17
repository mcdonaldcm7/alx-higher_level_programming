#!/usr/bin/python3
"""
This module uses the MySQLdb to connect to the database passed as argument and
prints all the cities of the from the state passed as an argument in the
'hbtn_0e_4_usa' database.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)

    cur = conn.cursor()
    sql_query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i:
            print(", ", end="")
        print(rows[i][0], end="")
    print()

    cur.close()
    conn.close()
