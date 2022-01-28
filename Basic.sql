create database payroll_services;
use payroll_services;

create table employee_payroll(id int primary key, Name varchar(20), Salary float, StartDate date);
insert into employee_payroll values( 1,'Gyanendra', 80000.00, '2021-12-13');
insert into employee_payroll values( 2,'Mohan', 70000.00, '2021-12-14');
insert into employee_payroll values( 3,'Sohan', 60000.00, '2021-12-16');
insert into employee_payroll values( 4,'Rohan', 50000.00, '2021-12-18');

select * from employee_payroll; # It will Display All Data from table
select Salary from employee_payroll WHERE name  = 'Gyanendra';
select Salary from employee_payroll WHERE name  = 'Mohan';
select Salary from employee_payroll WHERE id  = 4;

select * from employee_payroll where StartDate Between '2021-12-13' and '2021-12-13';

Alter table employee_payroll Add gender char(1);
UPDATE employee_payroll Set gender='M' where id = 1;
UPDATE employee_payroll Set gender ='M' where id = 2;
UPDATE employee_payroll Set gender ='M' where id = 3;
UPDATE employee_payroll Set gender ='M' where id = 4;

select SUM(Salary) from employee_payroll where gender = 'M' Group by gender;
select AVG(Salary) from employee_payroll where gender = 'M' Group by gender;
select MIN(Salary) from employee_payroll where gender = 'M' Group by gender;
select MAX(Salary) from employee_payroll where gender = 'M' Group by gender;
select SUM(Salary) from employee_payroll where gender = 'M' Group by gender;

Alter table employee_payroll Add phone bigint;
UPDATE employee_payroll Set phone=7440922090 where id = 1;
UPDATE employee_payroll Set phone=7440898989 where id = 2;
UPDATE employee_payroll Set phone=8790898989 where id = 3;
UPDATE employee_payroll Set phone=9876898989 where id = 4;
Alter table employee_payroll Add Address varchar(200) not null default 'Rewa';
Alter table employee_Payroll Add Department varchar(200) not null default'HR';
select * from employee_payroll;

create table Department(id int primary key, DepName varchar(20), Depid int, foreign key(Depid) references employee_payroll(id));
insert into Department values(502,'IT',1);
insert into Department values(708,'Accountant',2);
insert into Department values(908,'Attendees',3);
insert into Department values(1132,'Payroll',4);
select * from Department;
desc Department; # Discription of Table

select employee_Payroll.id, employee_Payroll.Name, Department.DepName from employee_payroll, Department where employee_Payroll.id=Department.id; # Join two tables

