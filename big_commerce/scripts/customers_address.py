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
	
	ordercount = int(math.ceil((bigcommerce.Customers_Address.get_count().count)/200.0))
	
	col = ['id',
               'customer_id',
               'first_name',
               'last_name',
               'company',
               'street_1',
               'street_2',
               'city',
               'state',
               'zip',
               'country',
               'country_iso2',
               'phone']
	
	a=[col]
	
	data = []
	
	for n in xrange(1,ordercount+1):
		orders = bigcommerce.Customers_Address.get(n)
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

a ='/home/mjhabiger/bigcommerce/hist_data/Customers_Address%s.txt' % date

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

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Customers_Address.txt') 


		
		
                
	
	
	
	
