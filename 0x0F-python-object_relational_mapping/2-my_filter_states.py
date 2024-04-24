#!/usr/bin/python3
"""
Displays the first occurrence of the state where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    # Define the SQL query with user input
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC LIMIT 1"

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query with the state name provided as input
    cursor.execute(query, (state_name,))

    # Fetch the first row from the result set
    row = cursor.fetchone()

    # Display the result
    if row:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
