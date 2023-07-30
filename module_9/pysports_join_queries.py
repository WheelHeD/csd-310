"""
 Title: pysports_join_queries.py
 Author: Will Head
 Date: 29 July 2023
 Description: Python program used to join the player and team tables
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

    # inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # results from inner join
    players = cursor.fetchall()

    print("\n ---Displaying Player Records---")

    # go through player data and display results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

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
