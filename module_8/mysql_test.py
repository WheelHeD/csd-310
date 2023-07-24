"""
    Title: mysql_test.py
    Author: Will Head
    Date: 20 July 2023
    Description: Program for testing connection to pysports database
"""
# import statements

import mysql.connector
from mysql.connector import errorcode

# database config object

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# try/catch block for handling MySQ errors

try:
    
    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    # show connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

# close database connection
finally:

    db.close()