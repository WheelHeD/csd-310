"""
 Title: pysports_queries.py
 Author: Will Head
 Date: 23 July 2023
 Description: Python program used to query a MySQL database
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

# try/catch block for handling MySQL errors

try:
    db = mysql.connector.connect(**config) # connect to pysports database

    cursor = db.cursor()

    # select query for team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # show results from cursor variable
    teams = cursor.fetchall()

    print("\n  ---Displaying Team Records---")

    # go through teams data and show the results
    for team in teams:
        print( " Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get results from cursor variable
    players = cursor.fetchall()

    print ("\n  ---Displaying Player Records---")

    # go through player data and show the results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n Press any key to continue... ")

# error handling
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" That database does not exist")

    else:
        print(err)

# close database connection
finally:
    db.close()