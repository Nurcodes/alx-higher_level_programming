#!/usr/bin/python3

''' This module only lists states starting with
N from a db using mysqldb
'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3])
    cur = conn.cursor()
    cur.execute(
            "SELECT id, name FROM `states` WHERE name \
                    LIKE 'N%' ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()
