use charming;
drop table if exists rewards_earners;
create table rewards_earners(customer_id int(10) unsigned,
 							 field2 int(10) unsigned,
 							 field3 int(10) unsigned,
 							 field4 decimal(12,6)) engine = MyISAM;