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
	
	ordercount = int(math.ceil((bigcommerce.Ordersproducts.get_count().count)/200.0))
	
	col = ['id',
               'order_id',
               'product_id',
               'order_address_id',
               'name',
               'sku',
               
'type',
               'base_price',
               'price_ex_tax',
               'price_inc_tax',
               
'price_tax',
               
'base_total',
               
'total_ex_tax',
               
'total_inc_tax',
               'total_tax',
               'weight',
               
'quantity',
               
'base_cost_price',
               
'cost_price_inc_tax',
               
'cost_price_ex_tax',
               
'cost_price_tax',
               
'is_refunded',
               
'refund_amount',
               'return_id',
               'wrapping_name',
               'base_wrapping_cost',
               'wrapping_cost_ex_tax',
               'wrapping_cost_inc_tax',
               
'wrapping_cost_tax',
               'wrapping_message',
               'quantity_shipped',
               
'event_name',
               'event_date',
               'fixed_shipping_cost',
               'ebay_item_id',
               
'ebay_transaction_id',
               'option_set_id',
               'parent_order_product_id',
               
'is_bundled_product ',
               'bin_picking_number',
               'applied_discounts',
               'product_options',
               'configurable_fields']
	
	a=[col]
	
	data = []
	
	for n in xrange(1,ordercount+1):
		orders = bigcommerce.Ordersproducts.get(n)
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

app= [['discount_amount','discount_type']]
for d in data[1:]:
	v=d[41]
	y=[]
	if len(v)==0:
		y=['','']
	else:	
		for i in v[0].itervalues():
			y.append(str(i))
	app.append(y)
i=0

for v in app:
	data[i].pop(41)
	for a in v:
		data[i].insert(41,a)
	i=i+1

now = datetime.datetime.now()

date = now.strftime("%Y%m%d")

a ='/home/mjhabiger/bigcommerce/hist_data/Orders_Products%s.txt' % date

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

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Orders_Products.txt') 

		
	

                
	
	
	
	
