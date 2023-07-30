"""
 Title: pysports_update_and_delete.py
 Author: Will Head
 Date: 29 July 2023
 Description: Python program used to insert, update, and delete records from the pysports database
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

def show_players(cursor, title):
    # inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # show results from cursor objects
    players = cursor.fetchall()

    
    print("\n --- {} ---".format(title))

    # go through player data and show results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    # try/catch for handling MySQL errors
try: 
    db = mysql.connector.connect(**config)
    
    # get the cursor object
    cursor = db.cursor()

    # insert player 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)" "Values(%s, %s, %s)")

    # player data
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert player record
    cursor.execute(add_player, player_data)

    # commit to database
    db.commit()

    # show records in player table
    show_players(cursor, "Displaying Players After Insert")

    # update the new record
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # execute the updated record
    cursor.execute(update_player)

    # show records in player table
    show_players(cursor, "Displaying Players After Update")

    # delete player gollum
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    # execute delete 
    cursor.execute(delete_player)

    # show results from player table
    show_players(cursor, "Displaying Players After Delete")

    input("\n\n Press any key to continue...")

    #error handling
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password is invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else: 
        print(err)

# end database connection
finally: 
    db.close()

    




