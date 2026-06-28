CREATE DATABASE business_analytics;
USE business_analytics;
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(30),
    join_date DATE,
    salary DECIMAL(10,2),
    bonus DECIMAL(10,2),
    performance_score INT
);
INSERT INTO employees VALUES
(1,'Ram Kumar','IT','2022-01-15',50000,5000,95),
(2,'Priya Sharma','HR','2023-06-10',45000,NULL,88),
(3,'Kavin Raj','IT','2024-03-20',55000,3000,91),
(4,'John Peter','Finance','2021-08-12',60000,NULL,75),
(5,'Meena','HR','2025-02-18',48000,2500,98);

SELECT * FROM employees;

#RP-01: Generate a report showing employee name and joining date in DD-MM-YYYY format.
SELECT emp_name,
DATE_FORMAT(join_date,'%d-%m-%y') AS joining_date
FROM employees;
#RP-02: Display employees who joined in the current year.
SELECT *
FROM employees
WHERE YEAR(join_date)=YEAR(CURDATE());
#RP-03: Calculate how many days each employee has worked in the organization.
SELECT emp_name,
DATEDIFF(CURDATE(),join_date) AS days_worked
FROM employees;
#RP-04: Generate a report showing employee tenure in years.
SELECT emp_name,
TIMESTAMPDIFF(YEAR,join_date,CURDATE()) AS tenure_years
FROM employees;
#RP-05: Display employee salaries rounded to the nearest whole number.
SELECT ROUND(salary) as rounded_salary FROM employees;
#RP-06: Generate a report showing the highest salary in the company.
SELECT MAX(salary) AS highest_salary FROM employees;
#RP-07: Generate a report showing the average salary by department.
SELECT department,AVG(salary) as average_salary FROM employees
GROUP BY department;
#RP-08: Calculate total salary expenditure department-wise.
SELECT department,SUM(salary) as total_salary FROM employees
GROUP BY department;
#RP-09: Identify employees whose salary is above the company average.
SELECT emp_name,salary
FROM employees
WHERE salary >
(
SELECT AVG(salary)
FROM employees
);
#RP-10: Display Bonus Not Assigned instead of NULL bonus values.
SELECT emp_name,
IFNULL(bonus,'Bonus Not Assigned') AS bonus
FROM employees;
#RP-11: Generate a report showing Employee Name, Salary, Bonus, and Total Compensation.
SELECT emp_name,
salary,
IFNULL(bonus,0) AS bonus,
salary+IFNULL(bonus,0) AS total_compensation
FROM employees;
#RP-12: Classify employees as Outstanding, Excellent, Good, or Needs Improvement based on performance score.
SELECT emp_name,
performance_score,
CASE
WHEN performance_score>=90 THEN 'Outstanding'
WHEN performance_score>=80 THEN 'Excellent'
WHEN performance_score>=70 THEN 'Good'
ELSE 'Needs Improvement'
END AS performance_category
FROM employees;
#RP-13: Generate a performance report showing Employee Name, Performance Score, and Performance Category.
SELECT emp_name,
performance_score,
CASE
WHEN performance_score>=90 THEN 'Outstanding'
WHEN performance_score>=80 THEN 'Excellent'
WHEN performance_score>=70 THEN 'Good'
ELSE 'Needs Improvement'
END AS performance_category
FROM employees;
#RP-14: Identify employees eligible for promotion (Performance Score >= 90).
SELECT emp_name, performance_score
FROM employees
WHERE performance_score>=90;
#Executive Dashboard
#RP-15: Generate a dashboard containing Department, Employee Count, Average Salary, Highest Salary, and Lowest Salary.
SELECT
    department,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employees
GROUP BY department;
#RP-16: Identify the department with the highest average salary.
SELECT department,
       AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC
LIMIT 1;
#RP-17: Identify the department with the highest-performing employee.
SELECT department,
       emp_name,
       performance_score
FROM employees
WHERE performance_score =
(
    SELECT MAX(performance_score)
    FROM employees
);
