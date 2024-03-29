#!/usr/bin/python3
"""
This is a module documentation for my file
"""
import MySQLdb
import sys


def sql_script() -> None:
    """
    sql_script function:
            A wrapper function tobe called when the file is executed
            from the command line
    :return: Nothing
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         password=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id = "
                "(SELECT states.id FROM states WHERE states.name = %s) ORDER "
                "BY cities.id", (state_name,))
    result = cur.fetchall()
    for row in result:
        if row != result[-1]:
            print(row[0], end=', ')
        else:
            print(row[0], end='')
    print('')
    cur.close()
    db.close()


if __name__ == "__main__":
    sql_script()
