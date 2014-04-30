use charming;
drop table if exists reporting_promo_history;

create table reporting_promo_history (promotion_id int(10) unsigned,
	  								  transaction_date datetime,
	  								  promoted_retail decimal(10,2),
	  								  non_promoted_retail decimal(10,2) unsigned,
	  								  promoted_cost	decimal(10,2),
	  								  non_promoted_cost	decimal(10,2),
	  								  no_transactions int(10) unsigned,
	  								  promoted_retail_with_cost decimal(10,2),
	  								  non_promoted_retail_with_cost	decimal(10,2),	  								 
	  								  rpromoted_retail	decimal(10,2),
	  								  rnon_promoted_retail decimal(10,2),
	  								  rpromoted_cost decimal(10,2),
	  								  rnon_promoted_cost decimal(10,2),
	  								  rpromoted_retail_with_cost decimal(10,2),
	  								  rnon_promoted_retail_with_cost decimal(10,2),
	  								  rno_transactions int(10)) engine = MyISAM;
