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
	
	ordercount = int(math.ceil((bigcommerce.Orders_Shippingaddress.get_count().count)/200.0))
	
	col = ['id',
               'order_id',
               'first_name',
               'last_name',
               'company',
               'street_1',
               'street_2',
               'city',
               'zip',
               'country',
               'country_iso2',
               'state',
               'email',
               'phone',
               'items_total',
               'items_shipped',
               'shipping_method',
               'base_cost',
               'cost_ex_tax',
               'cost_inc_tax',
               'cost_tax',
               'cost_tax_class_id',
               'base_handling_cost',
               'handling_cost_ex_tax',
               'handling_cost_inc_tax',
               'handling_cost_tax',
               'handling_cost_tax_class_id',
               'shipping_zone_id',
               'shipping_zone_name']
	
	a=[col]
	
	data = []
	
	for n in xrange(1,ordercount+1):
		orders = bigcommerce.Orders_Shippingaddress.get(n)
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

now = datetime.datetime.now()

date = now.strftime("%Y%m%d")

a ='/home/mjhabiger/bigcommerce/hist_data/Orders_Shippingaddress%s.txt' % date

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

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Orders_Shippingaddress.txt') 


		
		
                
	
	
	
	
