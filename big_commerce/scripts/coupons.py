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
	
	col = ['id',
               'name',
               'type',
               'amount',
               'min_purchase',
               'expires',
               'enabled',
               'code',
               'applies_to',
               'num_uses',
               'max_uses',
               'max_uses_per_customer',
               'restricted_to',
               'shipping_methods']
	
	a=[col]
	
	data = []
	
	for n in xrange(1,ordercount+1):
		orders = bigcommerce.Coupons.get(n)
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

bill=[]


app= [['ids','entity']]
for d in data[1:]:
	v=d[9]
	y=[]
	if type(v)==list:
		y=['','']
	else:	
		for i in v.itervalues():
			y.append(str(i))
	app.append(y)

res=[['restricted_to']]
for d in data[1:]:
	t=d[13]
	y=[]
	if type(t)==list:
		y=['']
	else: 
		for i in t.itervalues():
			y.append(str(i))
	res.append(y)


i=0

for v in app:
	data[i].pop(9)
	for a in v:
		data[i].insert(9,a)
	i=i+1

i=0

for v in res:
	data[i].pop(14)
	for a in v:
		data[i].insert(14,a)
	i=i+1

now = datetime.datetime.now()

date = now.strftime("%Y%m%d")

a ='/home/mjhabiger/bigcommerce/hist_data/Coupons%s.txt' % date

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

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Coupons.txt') 


		
                
	
	
	
	
