create database student_attendance;
use student_attendance;

create table student_data(id int auto_increment, primary key(id), name varchar(100), rollNo int, section varchar(1));
desc student_data;
select * from student_data;