#!/usr/bin/python3
''' Lists all cities by state '''
import MySQLdb
import sys


def show_states():
    if ';' not in sys.argv[4]:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.name " +
                    "FROM cities LEFT JOIN states " +
                    "ON cities.state_id = states.id " +
                    "WHERE states.name = '{}';".format(sys.argv[4]))
        query_rows = cur.fetchall()
        print(", ".join([row[0] for row in query_rows]))
        cur.close()
        db.close()

if __name__ == '__main__':
    show_states()
