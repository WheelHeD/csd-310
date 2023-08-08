""" 
    Title: whatabook.py
    Author: Will Head
    Date: 7 August 2023
    Description: Will's WhatABook Application- A program used to interface with a MySQL database
"""

# import statements
import sys
import mysql.connector
from mysql.connector import errorcode

# database config object 
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n  --- Main Menu --- \n")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program \n")

    try:
        choice = int(input('<Please Select Option 1-4>: '))

        return choice
    except ValueError:
        print("\n  Invalid number, terminating program...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # show results from the cursor object 

    books = _cursor.fetchall()

    print("\n  --- DISPLAYING BOOK LIST --- \n")
    
    # go through book data and show results  

    for book in books:
        print(" Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  --- DISPLAYING STORE LOCATIONS --- \n")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    """ validate the users ID """

    try:
        user_id = int(input('\n  Please enter a customer id number <Example: Type 1 for customer 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, terminating program...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, terminating program...\n")

        sys.exit(0)

def show_account_menu():

    """ display account menu """

    try:
        print("\n      --- Customer Menu --- \n")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu \n")
        account_option = int(input(' <Please Select Option 1-3>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, terminating program...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):

    """ query the database for a list of books that have been added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        --- DISPLAYING WISHLIST ITEMS ---")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):

    """ query the database for books that are not already in the users wishlist """

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        --- DISPLAYING AVAILABLE BOOKS --- \n")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    """ try/catch block for handling MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to WhatABook database 

    cursor = db.cursor() # cursor for queries

    print("\n  Thank You For Choosing Will's WhatABook Application! ")

    user_selection = show_menu() # show the menu 

    # while the user does not select 4
    while user_selection != 4:

        # if option 1 is selected, call show_books method and show the books
        if user_selection == 1:
            show_books(cursor)

        # if option 2 selected, call show_locations method and show locations
        if user_selection == 2:
            show_locations(cursor)

        # if option 3 is selected, call validate_user method to validate the user_id 
        # call show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option is not equal to 3
            while account_option != 3:

                # if option 1 is selected, call show_wishlist() method to show the current users 
                # show configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if option 2 is selected, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # input the entered book_id 
                    book_id = int(input("\n        Enter the id number of the book you want to add: "))
                    
                    # add selected book to users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit changes to database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid selection, please try again...")

                # show account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please try again...")
            
        # show main menu
        user_selection = show_menu()

    print("\n\n  Terminating program...")

except mysql.connector.Error as err:
    """ error handling """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  That database does not exist")

    else:
        print(err)

finally:

    """ close database connection """

    db.close()