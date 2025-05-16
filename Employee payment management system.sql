CREATE DATABASE IF NOT EXISTS payment_system;
USE payment_system;

CREATE TABLE IF NOT EXISTS employee_payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    company VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(20),
    hours_worked FLOAT,
    hourly_rate FLOAT,
    overtime FLOAT,
    tax FLOAT,
    gross_pay FLOAT,
    net_pay FLOAT,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

