#!/usr/bin/python3

import MySQLdb
import sys

'''
a script that lists all
states
'''

usr = sys.argv[1]
pss = sys.argv[2]
d = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=usr,
            password=pss, db=d)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
