-- MySQL Practice 

USE sql_store;

-- AND -- 
SELECT *
FROM order_items
WHERE order_id = 6 AND (unit_price * quantity) > 30;


-- AS --
SELECT 
	last_name, 
	first_name, 
	points, 
    (points+10)*100 AS discount_factor
FROM customers;

SELECT 
	name, 
	unit_price, 
    unit_price*1.1 AS 'new price'
FROM products;


-- IN --
SELECT *
FROM products
WHERE quantity_in_stock IN (49,38,72);


-- BETWEEN --
select * 
from customers
where birth_date between '1990-01-01' and '2000-01-01' ;


-- LIKE --
-- '%' sign means any number of chars, while # of '_' signs specifies how many chars
select * 
from customers
where last_name like '%d%'; -- 'd' somewhere in their last name
-- where last_name like '_y' -- ends with 'y' and is two chars long

select * 
from customers
where address like '%trail%' or address like '%avenue%';
-- where phone like '%9'


-- REGEXP --

select * 
from customers
where last_name regexp 'field|mac|rose'; -- '|' is logical 'OR'

select * 
from customers
where last_name regexp '[gim]e'; -- if there is 'ge', 'ie', or 'me' in last_name
-- or you can do from, say 'c' to 'h':
-- where last_name regexp '[c-h]e' 

select *
from customers
where first_name regexp 'elka|ambur'; 

select *
from customers
where last_name regexp 'ey$|on$';

select *
from customers
where last_name regexp '^my|se';

select *
from customers
where last_name regexp 'b[ru]';
-- or:
-- where last_name regexp 'br|bu' 


-- IS NULL --
select *
from customers 
where phone is not null;

select * from orders
where shipped_date is null;


-- ORDER BY --
select * from customers
order by first_name desc;

select *, points+10 as new_points
from customers
order by birth_date, last_name;


-- TEST QUESTION --
select *, quantity*unit_price as total_price
from order_items
where order_id = 2
order by total_price desc;


-- LIMIT (should always come last)  -- 
select *
from customers
limit 300;

select *
from customers
limit 6, 3; -- skip the first 5 elements and take the next 3


-- TEST -- 
-- get the most loyal customers (highest points) --
select *
from customers
order by points desc
limit 3;


-- INNER JOINS AND MORE ALIASES--
select order_id, first_name, o.customer_id, last_name
from orders o
join customers c on o.customer_id = c.customer_id;


-- TEST --
SELECT order_id, oi.product_id, quantity, oi.unit_price
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;










