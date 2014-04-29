use charming;
drop table if exists reporting_attrib_codes;
create table reporting_attrib_codes(customer_id	int(10) unsigned,
                                    attribute_grouping_code	char(4),
                                    attribute_code char(5),
                                    attribute_comment varchar(32),
                                    attribute_value	tinyint(1) unsigned,
                                    attribute_date	date,
                                    timestamp timestamp) engine = MyISAM;