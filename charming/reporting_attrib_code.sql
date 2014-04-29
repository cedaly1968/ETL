use charming;
drop table if exists reporting_attrib_code;

create table reporting_attrib_code(attribute_grouping_code char(4),
	                               attribute_grouping_description varchar(32),
	                               attribute_unique_flag tinyint(1) unsigned,
	                               attribute_instore_cps_flag tinyint(1) unsigned,
	                               attribute_comment_default char(4),
	                               attribute_date_default char(4),
	                               attribute_value_default char(4),
	                               attribute_code_label	varchar(32),
	                               attribute_comment_label char(4),
	                               attribute_date_label	char(4),
	                               attribute_value_label char(4),
	                               merge_override tinyint(1) unsigned,
	                               ignore_blank	tinyint(1) unsigned,
	                               summary_visible tinyint(1) unsigned,
	                               timestamp timestamp) engine = MyISAM;

