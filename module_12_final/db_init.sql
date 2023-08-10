/*
    Title: db_init.sql
    Author: Will Head
    Date: 2 August 2023
    Description: Initialization script for WhatABook database
*/

-- drop user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and assign password 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to whatabook database to whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create tables
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('3159 W 11th St, Cleveland, OH 44109');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Little Engine That Could', 'Watty Piper', 'Tale of a little engine pulling a train over a mountain');

INSERT INTO book(book_name, author, details)
    VALUES('Green Eggs and Ham', 'Dr. Seuss', 'Story to get kids to try new foods');

INSERT INTO book(book_name, author, details)
    VALUES('Diary of a Wimpy Kid', 'Jeff Kinney', "A kid dealing with being a kid");

INSERT INTO book(book_name, author)
    VALUES('Charlie and the Chocolate Factory', 'Roald Dahl');

INSERT INTO book(book_name, author)
    VALUES('The Wizard of OZ', 'L. Frank Baum');

INSERT INTO book(book_name, author)
    VALUES("The Very Hungry Caterpillar", 'Eric Carle');

INSERT INTO book(book_name, author)
    VALUES('The Tale of Peter Rabbit', 'Beatrix Potter');

INSERT INTO book(book_name, author)
    VALUES('Curious George', 'H.A. Rey');

INSERT INTO book(book_name, author)
    VALUES('Where the Wild Things Are', 'Maurice Sendak');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Tony', 'Stark');

INSERT INTO user(first_name, last_name)
    VALUES('Bruce', 'Banner');

INSERT INTO user(first_name, last_name)
    VALUES('Peter', 'Parker');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Tony'), 
        (SELECT book_id FROM book WHERE book_name = 'Green Eggs and Ham')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bruce'),
        (SELECT book_id FROM book WHERE book_name = 'Diary of a Wimpy Kid')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Peter'),
        (SELECT book_id FROM book WHERE book_name = 'Curious George')
    );