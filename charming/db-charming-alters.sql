use charming;

alter table reporting add index indx_trans_id (transaction_id);
alter table reporting add index indx_trans_date (transaction_date);

alter table reporting_attrib_code add index indx_attrib_code (attribute_grouping_code);

alter table reporting_attrib_codes add index indx_customer_id (customer_id);
alter table reporting_attrib_codes add index indx_attrib_code (attribute_grouping_code);
alter table reporting_attrib_codes add index indx_attrib_code2 (attribute_code);

alter table reporting_details add index indx_trans_id (transaction_id);

alter table reporting_promo add index indx_promo_id (promotion_id);
alter table reporting_promo add index indx_promo_desc (promotion_description);
alter table reporting_promo add index indx_start_date (start_date);
alter table reporting_promo add index indx_end_date (end_date);

alter table reporting_promo_coupon add index indx_promo_id (promotion_id);
alter table reporting_promo_coupon add index indx_coupon_code (coupon_code);

alter table reporting_promo_customer add index indx_promo_id (promotion_id);
alter table reporting_promo_customer add index indx_customer_id (customer_id);

alter table reporting_promo_history add index indx_promo_id (promotion_id);
alter table reporting_promo_history add index indx_transaction_date(transaction_date);

alter table reporting_promo_list add index indx_promo_id (promotion_id);
alter table reporting_promo_list add index indx_list_code (list_code);

alter table rewards_earners add index indx_customer_id (customer_id);
