#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database
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

    # Define the SQL query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query
    cursor.execute(query)

    # Initialize a set to store unique states
    unique_states = set()

    # Display the results
    for row in cursor.fetchall():
        state_id, state_name = row
        if state_name not in unique_states:
            unique_states.add(state_name)
            print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
