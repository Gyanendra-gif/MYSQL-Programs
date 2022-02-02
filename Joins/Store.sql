create database store;
use store;

create table items(id int auto_increment, primary key(id), product_name varchar(50), price float, quantity int);
insert into items (product_name,price,quantity) values ('HP', 30000.00, 2);
insert into items (product_name,price,quantity) values ('DELL', 40000.00, 3);
insert into items (product_name,price,quantity) values ('LENOVO', 50000.00, 4);
insert into items (product_name,price,quantity) values ('SONY', 60000.00, 5);

create table customer(cid int ,foreign key(cid)references items(id), name varchar(50), city varchar(50));
insert into customer values (1, 'Sam','Mumbai');
insert into customer values (2, 'Tom','Delhi');
insert into customer values (3, 'Harry','Banglore');
insert into customer values (4, 'Sam','Pune');
