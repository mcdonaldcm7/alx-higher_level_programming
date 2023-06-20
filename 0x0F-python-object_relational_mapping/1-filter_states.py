#!/usr/bin/python3
"""
This module uses the MySQLdb to connect to the database passed as argument and
prints all the states of the 'hbtn_0e_0_usa' database that begin with the
letter 'N'
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
    query = "\
    SELECT * FROM states \
    WHERE name COLLATE utf8mb4_bin LIKE 'N%' \
    ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
