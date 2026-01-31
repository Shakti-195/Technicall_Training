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

create Table orders(
product_id  varchar (50),
product_name varchar(50),
price int ,
order_id int primary key,
customer_id varchar(50) 
);
show databases;
use company;

insert into orders values
("P1","Phone",500,1,"C101"),
("P2","Laptop",700,2,"C102"),
("P3","Tablet",300,3,"C101")
;


select * from orders;


SELECT 
    customers.customer_name,
    orders.product_name,
    orders.price
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;


SELECT DISTINCT customer_id FROM customers;
SELECT DISTINCT customer_id FROM orders;
