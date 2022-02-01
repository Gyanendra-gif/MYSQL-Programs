use demo;
create table List(id int auto_increment, primary key(id), name varchar(50), data varchar(50));

insert into List(name, data) values('Tom','IT');
insert into List(name, data) values('Sam','HR');
insert into List(name, data) values('Karan','AC');
insert into List(name, data) values('Mac','DEP');
select * from List;
select * from List where data='AC';
update List set data = 'PY' where id=3;

create table City(Cid int , name varchar(50), foreign key(Cid) references List(id));
desc City;

insert into City value(1, 'Delhi');
select * from City;

select list.name, City.name from list, City where City.Cid=List.id;

select * from payroll_services.employee_payroll;
