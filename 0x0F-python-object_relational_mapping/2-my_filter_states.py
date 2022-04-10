#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host=("localhost"),
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()

    for row in query_rows:
        if (sys.argv[4] == row[1]):
            print(row)

    cursor.close()
    db.close()
