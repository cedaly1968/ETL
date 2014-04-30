use charming;
drop table if exists reporting_promo_coupon;
create table reporting_promo_coupon(promotion_id int(10) unsigned,
             						coupon_code varchar(32),
             						coupon_description varchar(128),
             						list_code smallint(5)) engine = MyISAM;
