#!/usr/bin/python3
''' Lists all cities by state '''
import MySQLdb
import sys


def show_states():
    if len(sys.argv) == 4:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name " +
                    "FROM states LEFT JOIN cities " +
                    "ON cities.state_id = states.id " +
                    "ORDER BY cities.id;")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        db.close()

if __name__ == '__main__':
    show_states()
