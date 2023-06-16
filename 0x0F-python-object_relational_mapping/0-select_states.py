#!/usr/bin/python3
"""
This module uses the MySQLdb to connect to the database passed as argument and
prints all the states of the 'hbtn_0e_0_usa' database
"""


import MySQLdb
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, password=pwd, database=db)

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
