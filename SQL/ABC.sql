CREATE DATABASE ABC_Corporation;
USE ABC_Corporation;
CREATE TABLE employee_master(
emp_id INT,
emp_name VARCHAR(50),
email VARCHAR(100),
mobile VARCHAR(20),
department VARCHAR(30),
city VARCHAR(50)
);
INSERT INTO employee_master VALUES
(1, 'ram kumar','RAM@GMAIL.COM','9876543210','IT','chennai'),
(2,'Priya Sharma','PRIYA@YAHOO.COM','9876543211','HR','CHENNAI'),
(3,'kavin raj','kavin@gmail.com','9876543212','IT','Coimbatore'),
(4,'John Peter',NULL,'9876543213','Finance','MUMBAI'),
(5,'MEENA','MEENA@GMAIL.COM','9876543214','HR','coimbatore');
SELECT * FROM employee_master;
#DC-01: Generate employee names without leading or trailing spaces.
SELECT TRIM(emp_name) AS employee_name FROM employee_master;
#DC-02: Standardize all employee names into uppercase format.
SELECT emp_name,UPPER(emp_name) AS UPPER_CASE FROM employee_master;
#DC-03: Standardize all email addresses into lowercase format.
SELECT email,LOWER(email) AS LOWERCASE FROM employee_master;
#DC-04: Generate a report showing the number of characters in each employee name.
SELECT emp_name,LENGTH(emp_name) AS emp_name_length FROM employee_master;
#DC-05: Identify employees whose names exceed 10 characters.
SELECT emp_name FROM employee_master
WHERE LENGTH(emp_name)>10;
#DC-06: Generate a list of employees whose email address belongs to Gmail.
SELECT emp_name,email FROM employee_master
WHERE email LIKE '%@GMAIL.COM';
#DC-07: Generate a list of employees whose names begin with the letter M.
SELECT emp_name FROM employee_master
WHERE emp_name LIKE'M%';
#DC-08: Display the first 5 characters of every employee name.
SELECT emp_name, LEFT(emp_name,5) AS FIRST_5_character FROM employee_master;
#DC-09: Display the last 4 digits of each employee mobile number.
SELECT mobile, RIGHT(mobile,4) AS mobile_last_4digit FROM employee_master;
#DC-10: Generate a report showing employee name and city in the format EMPLOYEE_NAME- CITY.
SELECT emp_name,city, CONCAT(emp_name,'-',city) AS EMPLOYEE_NAME_CITY FROM employee_master;
#DC-11: Generate an output where the city name CHENNAI is displayed as CHENNAI HQ.
SELECT REPLACE(city,'CHENNAI','CHENNAIHQ') AS city_name FROM employee_master;
#DC-12: Generate employee email addresses. If an email address is missing, display Email Not Available.
SELECT emp_name,email,IFNULL(email,'Emil not available') AS email_adress FROM employee_master;
#DC-13: Generate a unique list of cities available in the employee database.
SELECT DISTINCT city FROM employee_master;
#DC-14: Identify employees whose email address is missing.
SELECT emp_name,email FROM employee_master 
WHERE email IS NULL;

#DC-15: Generate a migration-ready employee report containing Employee Name, Email
#Address, Department, City, and Email Status.
	SELECT emp_name AS Employee_Name,
	email AS Email_Address,department,city,
	CASE 
	WHEN email IS NULL THEN 'Missing'
	ELSE'Available'
	END AS email_status
	FROM employee_master;
#DC-18: Generate employee usernames using the first three letters of the employee name and last four digits of the mobile number.
SELECT emp_name,mobile,
CONCAT(LEFT(emp_name,3),RIGHT(mobile,4)) AS USERNAME FROM employee_master;
#DC-19: Generate a city-wise employee count report.
SELECT city, COUNT(*) AS employee_count
FROM employee_master
GROUP BY city;
#DC-20: Generate a department-wise employee count report.
SELECT department,COUNT(*) AS employee_count
FROM employee_master
GROUP BY department;