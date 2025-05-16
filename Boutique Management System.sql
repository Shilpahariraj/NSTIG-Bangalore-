CREATE DATABASE sboutique;
USE sboutique;

create table customer (
    cust_id int(8) PRIMARY KEY,
    c_nam varchar(30),
    c_lnam varchar(30),
    c_phno varchar(10),
    c_adrs varchar(50),
    bkd_pro varchar(40) );
    
    create table employee (
    emp_id char(3) PRIMARY KEY,
    e_nam varchar(30),
    e_lnam varchar(30),
    e_phno varchar(10),
    e_adrs varchar(30));
    
    create table products (
    pro_num char(5),
    pro_id char(10) PRIMARY KEY,
    pro_price int(6),
    pro_stk int(5) );
    
    INSERT INTO products VALUES
('1','KWPTP25',330,18),
('2','KWPTP30',450,30),
('3','KWPTP45',650,20),
('4','SSST025',850,10),
('5','SSST030',350,12);

USE sboutique;
SHOW TABLES;

DESC customer;

DESC employee;

DESC products;

SELECT * FROM products;

