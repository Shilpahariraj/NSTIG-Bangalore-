CREATE DATABASE students_db;
SHOW DATABASES;
USE student;
CREATE TABLE Studs (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100),
    Age INT,
    email VARCHAR (100)
);
INSERT INTO Studs (StudentID, FirstName, Age, Email)
VALUES 
(1, 'Anand', 22, 'anand@example.com'),
(2, 'Sunil', 21, 'sunil@example.com'),
(3, 'Rahul', 23, 'rahul@example.com'),
(4, 'Sneha', 20, 'sneha@example.com'),
(5, 'Amit', 24, 'amit@example.com');
SELECT * FROM Studs;

DROP TABLE Course;
CREATE TABLE IF NOT EXISTS Coursess (
    Course_id INT AUTO_INCREMENT PRIMARY KEY,
    Course_name VARCHAR(100)
);
SELECT * FROM Coursess;
INSERT INTO Coursess (Course_id, Course_name)
VALUES 
  (55, 'Mathematics'),
  (51, 'Physics'),
  (22, 'Chemistry'),
  (11, 'Biology'),
  (33, 'Computer Science');
SELECT * FROM Coursess;

CREATE TABLE Marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);