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
	
	ordercount = 1
	
	data = []
	
	
	orders = bigcommerce.Store.get()
	y= []
	for o in orders.iterkeys():
			y.append(str(o))
	data.append(y)

	y=[]
	
	for o in orders.itervalues():
			y.append(str(o))
	data.append(y)               

	for n in xrange(1, len(data)):
			data[n].insert(0,i[0])               

data[0].insert(0,'store_name')



now = datetime.datetime.now()

date = now.strftime("%Y%m%d")

a ='/home/mjhabiger/bigcommerce/hist_data/Store%s.txt' % date

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

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Store.txt') 


		
		
                
	
	
	
	
