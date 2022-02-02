create database Hotel;
use Hotel;

create table customer (cid int auto_increment,  primary key(cid), cname varchar(50), age int);

insert into customer(cname, age) value ('Mohan', 18);
insert into customer(cname, age) value ('Sohan', 28);
insert into customer(cname, age) value ('Rohan', 23);
insert into customer(cname, age) value ('Max', 18);
insert into customer(cname, age) value ('Anthony', 38);
insert into customer(cname, age) value ('Smith', 45);
insert into customer(cname, age) value ('Mac', 47);
insert into customer(cname, age) value ('Harry', 41);

select * from customer;