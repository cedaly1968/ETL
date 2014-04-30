use charming;
drop table if exists reporting_promo_customer;
create table reporting_promo_customer(customer_id int(10) unsigned,
	 								  promotion_id int(10) unsigned,
	 								  list_code	smallint(5) unsigned,
	 								  response_flag	smallint(5) unsigned,
	 								  household_mailed_flag	tinyint(1) unsigned) engine = MyISAM;
