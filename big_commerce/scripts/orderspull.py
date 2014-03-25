import bigcommerce
import math
import MySQLdb
import _mysql
import datetime
import csv

db = _mysql.connect("localhost",user="root",passwd="Economics1$&*",db="BigCommerce")

db.query("""Select store_address, username, api_key from dashfacts_Clients""")

store_list = db.store_result()

store_tuple = store_list.fetch_row()

for i in store_tuple:
	bigcommerce.Connection.api_key =i[2]
	
	bigcommerce.Connection.user =i[1]
	
	bigcommerce.Connection.host = i[0]
	
	ordercount = int(math.ceil((bigcommerce.Orders.get_count().count)/200.0))
	
	col = ['id'
	,'customer_id'
	,'date_created'
	,'date_modified'
	,'subtotal_ex_tax'
	,'subtotal_inc_tax'
	,'subtotal_tax'
	,'total_tax'
	,'base_shipping_cost'
	,'shipping_cost_ex_tax'
	,'shipping_cost_inc_tax'
	,'shipping_cost_tax'
	,'shipping_cost_tax_class_id'
	,'base_handling_cost'
	,'handling_cost_ex_tax'
	,'handling_cost_inc_tax'
	,'handling_cost_tax'
	,'handling_cost_tax_class_id'
	,'base_wrapping_cost'
	,'wrapping_cost_ex_tax'
	,'wrapping_cost_inc_tax'
	,'wrapping_cost_tax'
	,'wrapping_cost_tax_class_id'
	,'total_ex_tax'
	,'total_inc_tax'
	,'status_id'
	,'status'
	,'items_total'
	,'items_shipped'
	,'payment_method'
	,'payment_provider_id'
	,'payment_status'
	,'refunded_amount'
	,'order_is_digital'
	,'date_shipped'
	,'store_credit_amount'
	,'gift_certificate_amount'
	,'ip_address'
	,'geoip_country'
	,'geoip_country_iso2'
	,'currency_id'
	,'currency_code'
	,'default_currency_id'
	,'default_currency_code'
	,'currency_exchange_rate'
	,'staff_notes'
	,'customer_message'
	,'discount_amount'
	,'shipping_address_count'
	,'coupon_discount'
	,'is_deleted'
	,'billing_address']
	
	a=[col]
	
	data = []
	
	for n in xrange(1,ordercount+1):
		orders = bigcommerce.Orders.get(n)
		for o in orders:
			d=[]      
			for c in col: 
				b=getattr(o,c) 
				d.append(b)
			data.append(d)
 
	for n in xrange(0, len(data)):
		data[n].insert(0,i[0])

col.insert(0,'store_name')

data.insert(0,col)

bill = []

for d in data:
	t=d[52]
	bill.append(t)

bill = bill[1:]

t= []
for b in bill:
	y=[]
	for c in b.itervalues():
		y.append(str(c))
	t.append(y)

key =[]
for c in bill[0].iterkeys():
    key.append(str(c))

t.insert(0,key)   

i=0

for v in t:
	data[i].pop(52)
	for a in v:
		data[i].insert(52,a)
	i=i+1

now = datetime.datetime.now()

date = now.strftime("%Y%m%d")

a ='/home/mjhabiger/bigcommerce/hist_data/Orders%s.txt' % date

##data=str(data)

with open(a,'w') as the_file:
        csv.register_dialect("custom",delimiter="|", skipinitialspace=True)
        writer = csv.writer(the_file, dialect="custom")
        for t in data:
                writer.writerow(t)

##f = open(a, 'w') 

##f.write(data)

the_file.close()

import shutil

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Orders.txt') 


		
		
                
	
	
	
	
