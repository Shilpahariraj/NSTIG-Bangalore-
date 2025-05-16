CREATE DATABASE student_report_db;
USE student_report_db;

CREATE TABLE Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100)
);

CREATE TABLE Subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100)
);

CREATE TABLE Marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    marks_obtained FLOAT,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(id)
);