use charming;
drop table if exists reporting_details;
create table reporting_details(transaction_id int(10) unsigned,
	                           transaction_line_no int(10) unsigned,
	                           sale_or_return_indicator	char(1),
	                           sales_associate_no int(10) unsigned,
	                           style_id	int(10) unsigned,
	                           color_code smallint(5) unsigned,
	                           size_description	varchar(32),
	                           quantity	int(5) unsigned,
	                           net_retail decimal(7,2),
	                           cost	decimal(7,2),
	                           markdown_percent	smallint(5) unsigned,
	                           coupon_code varchar(32),
	                           comments	text,
	                           promotion_flag smallint(5) unsigned,
	                           class_code int(10) unsigned,
	                           net_retail_central decimal(7,2)) engine=MyISAM;
