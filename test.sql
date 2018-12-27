#create database tmobile;

use tmobile;
#create table wipro(id int, first_name varchar(9), last_name varchar(10), designation varchar(20) )
## CRUD
#C -CREATE, R-READ, U-UPDATE, D-DELETE

##INSERT into wipro values(1, "venkat", "gandham", "lead");
##insert into wipro values(2, "anupam", "verma", "supervisor");wipro

##read

#SELECT * from wipro;
#update wipro set designation = "devops_engineer" where id = 1;

delete from wipro where first_name = "venkat";
delete from wipro where first_name = "anupam";


