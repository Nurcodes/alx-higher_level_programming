#!/usr/bin/python3

import MySQLdb
from sys import argv

''' This module only lists states starting with
N from a db using mysqldb
'''

if __name__ == '__main__':
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3])
    cur = conn.cursor()
    cur.execute(
            "SELECT id, name FROM `states` WHERE name \
                    LIKE BINARY 'N%' ORDER BY id ASC")
    db = cur.fetchall()
    for i in db:
        print(i)
    cur.close()
    conn.close()
