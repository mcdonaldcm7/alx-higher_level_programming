#!/usr/bin/python3
"""
This module uses the MySQLdb to connect to the database passed as argument and
prints all the states of the 'hbtn_0e_0_usa' database that matches the argument
passed to search for and does this is a way immune to SQL Injection
"""


import MySQLdb
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]

    conn = MySQLdb.connect(
            host='localhost', port=3306, user=usr, password=pwd, database=db)

    cur = conn.cursor()
    sql_query = f"SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(sql_query, (search_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
