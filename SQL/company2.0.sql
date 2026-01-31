show tables;

create table Customers(
customer_id  varchar(50) primary key,
customer_name varchar(50),
gender varchar (50),
city varchar (50),
signup_date date 
);

select * from Customers;

INSERT INTO Customers (customer_id, customer_name, gender, city, signup_date) VALUES
("C201", "Amit",   "Male",   "Delhi",      "2024-01-10"),
("C202", "Sneha",  "Female", "Mumbai",     "2024-02-15"),
("C203", "Ravi",   "Male",   "Bangalore",  "2024-03-05"),
("C204", "Pooja",  "Female", "Delhi",      "2024-03-20"),
("C205", "Karan",  "Male",   "Mumbai",     "2024-04-01");



CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(50),
    product_name VARCHAR(50),
    category VARCHAR(50),
    amount INT,
    order_date DATE
);

INSERT INTO orders VALUES
(101, 'C201', 'Laptop', 'Electronics', 55000, '2024-04-10'),
(102, 'C202', 'Mobile', 'Electronics', 25000, '2024-04-12'),
(103, 'C201', 'Mouse', 'Accessories', 800, '2024-04-15'),
(104, 'C203', 'Chair', 'Furniture', 4500, '2024-04-18'),
(105, 'C206', 'Table', 'Furniture', 7000, '2024-04-20'),
(106, 'C205', 'Headphones', 'Accessories', 3000, '2024-04-22');

select * from orders;

SELECT 
    c.customer_id,
    c.customer_name,
    o.product_name,
    o.category,
    o.amount,
    o.order_date
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;

SELECT 
    c.customer_name,
    o.product_name,
    o.amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT 
    c.customer_name,
    o.product_name,
    o.amount
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT 
    c.customer_name,
    o.product_name,
    o.amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT 
    c.customer_name,
    o.product_name,
    o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.category = 'Electronics';

SELECT 
    c.customer_name,
    SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name;



