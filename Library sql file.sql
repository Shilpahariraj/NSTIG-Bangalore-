CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;
 
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS IssueRecords (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

SELECT * FROM Books;
SELECT * FROM Members;
SELECT * FROM IssueRecords;
