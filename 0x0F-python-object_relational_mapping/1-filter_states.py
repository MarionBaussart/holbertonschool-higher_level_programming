#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

db = MySQLdb.connect(
    host=("localhost"),
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE states.name \
    LIKE 'N%' ORDER BY id ASC")
query_rows = cursor.fetchall()

for row in query_rows:
    print(row)

cursor.close()
db.close()
