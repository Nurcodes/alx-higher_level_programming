#!/usr/bin/python3

# This module shows states in a database using mysqldb

import MySQLdb
import sys

usr = sys.argv[1]
pss = sys.argv[2]
d = sys.argv[3]

db = MySQLdb.connect(host="localhost", user=usr, passwd=pss, db=d)

cur = db.cursor()

cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print("{}".format(row))
cur.close()
db.close()
