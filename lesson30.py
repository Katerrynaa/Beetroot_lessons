# практичне за 10.08
'''
SELECT * FROM patients LIMIT 10;

SELECT MAX(birth_date) FROM patients;

SELECT MIN(birth_date) FROM patients;

SELECT COUNT(doctor_id) FROM doctors;

SELECT * FROM patients WHERE first_name LIKE "A%";

SELECT * FROM patients LIMIT 100;

SELECT * FROM patients WHERE birth_date between "1990-01-01" AND "2010-01-01";

SELECT first_name, specialty FROM doctors;

SELECT first_name, last_name, city FROM patients WHERE allergies="Sulfa";

SELECT * FROM doctors WHERE last_name LIKE "Smith%";

SELECT * FROM province_names ORDER BY province_name ASC;

SELECT * FROM doctors WHERE last_name LIKE "%ko" ORDER BY last_name ASC;

SELECT * FROM patients WHERE birth_date BETWEEN "1950-01-01" AND "2020-01-01" LIMIt 5;

SELECT (patients.patient_id) AS patients_count, province_names.province_name 
FROM patients 
INNER JOIN province_names 
ON province_names.province_id = patients.province_id
LIMIT 50;

SELECT (patients.patient_id) AS patients_count, province_names.province_name
FROM patients
INNER JOIN province_names
ON province_names.province_id = patients.province_id
GROUP BY province_names.province_name
HAVING patients_count > 50;

SELECT (patients.patient_id) AS patients_count, province_names.province_name
FROM patients 
INNER JOIN province_names
ON province_names.province_id = patients.province_id
WHERE patients.birth_date between "1960-01-01" and "1980-01-01"
GROUP BY province_names.province_name
HAVING patients_count > 10 

'''

# практичне за 15.08
'''
SELECT category_id, description FROM categories GROUP BY category_name;

SELECT product_name, unit_price FROM products ORDER BY unit_price desc;

SELECT contact_name, address, city FROM customers WHERE NOT country = "Germany" 
AND NOT country = "Spain" AND NOT country = "Mexico";

SELECT contact_name, city, country FROM customers WHERE NOT country = "USA" AND NOT country = "Canada"
AND NOT country = "Mexico";

SELECT order_date, shipped_date, customer_id, freight from orders 
WHERE order_id
BETWEEN '2019-05-01' AND '2019-06-30';

SELECT order_date, shipped_date, customer_id, freight FROM orders
WHERE order_id LIKE "2018-02-26";

SELECT employee_id, order_id, customer_id, required_date, shipped_date FROM orders; 

SELECT company_name, contact_name, fax FROM customers WHERE fax IS NOT NULL;

SELECT employee_id, order_id, customer_id, required_date, shipped_date FROM orders;

SELECT supplier_id, company_name, phone from suppliers WHERE phone IS NOT NULL;

SELECT first_name, last_name, hire_date FROM employees WHERE hire_date<('2022-01-01');

SELECT product_name, quantity_per_unit, units_in_stock FROM products
WHERE units_in_stock < 10;

SELECT company_name, contact_name, contact_title FROM customers 
WHERE contact_title IS NOT NULL;

SELECT order_id, ship_country, ship_region from orders WHERE NOT ship_country = "USA"
AND ship_region IS NOT NULL;

SELECT employee_id, last_name, first_name FROM employees WHERE title="Sales Representative";

SELECT products.product_name, order_details.order_id, order_details.quantity
FROM order_details 
JOIN products ON order_details.product_id=products.product_id
WHERE order_details.quantity>1;

SELECT categories.category_name, products.quantity_per_unit
FROM categories
JOIN products ON categories.category_id=products.product_id 
LIMIT 10;

select employees.first_name, employees.hire_date, orders.order_date
FROM employees
JOIN orders ON employees.employee_id=orders.employee_id
WHERE order_date IS NULL;

SELECT customers.company_name, employees.first_name, employees.last_name, orders.order_date
FROM orders 
JOIN customers ON orders.customer_id=customers.customer_id
JOIN employees ON orders.employee_id=employees.employee_id
WHERE orders.order_date>(2010-01-01);

SELECT customers.company_name, suppliers.company_name, customers.customer_id, suppliers.supplier_id,
customers.city,suppliers.city
JOIN orders ON order_details.order_id=orders.order_id
JOIn customers ON customers.customer_id=orders.customer_id
JOIn products ON order_details.product_id=products.product_id
JOIN suppliers ON products.supplier_id=suppliers.supplier_id
WHERE customers.city = suppliers.city;

'''
