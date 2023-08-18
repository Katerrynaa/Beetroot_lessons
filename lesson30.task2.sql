SELECT first_name, last_name FROM employees;

SELECT department_id from employees;

SELECT * FROM employees ORDER BY first_name DESC;

SELECT first_name, last_name, salary from employees;

SELECT MIN(salary) from employees;

SELECT MAX(salary) from employees;

SELECT first_name, last_name, job_id, round(salary/12,2) as 'Montly Salary' from employees;
