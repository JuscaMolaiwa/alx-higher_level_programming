#!/usr/bin/python3
"""
Lists all states from the database
It takes 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute SQL query to select all states and sort them by id
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
