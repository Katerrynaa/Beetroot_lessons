SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
INNER JOIN department ON employees.department_id=department.department_id;

SELECT employees.first_name, employees.last_name, employees.department_id,
locations.city, locations.state_province
FROM employees
INNER JOIN department
ON employees.department_id=department.department_id
JOIN locations
ON department.location_id=locations.location_id;

SELECT employees.first_name, employees.last_name, employees.department_id,
department.department_name
FROM employees
INNER JOIN department
ON employees.department_id=department.department_id
WHERE department.department_id='80';

SELECT employees.first_name, employees.last_name, department.department_id, department.department_name
FROM employees
LEFT JOIN department 
ON employees.department_id=department.department_id;

SELECT job_title, first_name || ' ' || last_name as employee_name, max_salary
FROM employees
JOIN jobs;

SELECT job_title, AVG(salary)
FROM employees
JOIN JOBS 
GROUP BY job_title;

SELECT first_name || ' ' || last_name AS employee_name, salary
FROM employees
JOIN department.department_id
JOIN locations.location_id
WHERE city='London';

SELECT COUNT(employees.first_name) AS employees_count, department.department_name
FROM employees
JOIN department ON department.department_id=employees.department_id;