use charming;
drop table if exists reporting_promo_list;
create table reporting_promo_list(promotion_id int(10) unsigned,
	 							  list_code	int(10) unsigned,
	 							  source_code varchar(64),
	 							  list_description varchar(128),
	 							  selection_id int(10) unsigned,
	 							  control_group_flag smallint(5) unsigned,
	 							  control_group_for_list_code smallint(5) unsigned) engine = MyISAM;
