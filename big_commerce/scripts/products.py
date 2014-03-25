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
	
	ordercount = int(math.ceil((bigcommerce.Products.get_count().count)/200.0))
	
	col = ['id',
               'keyword_filter',
               'name',
               'type',
               'sku',
               'description',
               'search_keywords',
               'availability_description',
               'price',
               'cost_price',
               'retail_price',
               'sale_price',
               'sort_order',
               'is_visible',
               'is_featured',
               'related_products',
               'inventory_level',
               'inventory_warning_level',
               'warranty',
               'weight',
               'width',
               'height',
               'depth',
               'fixed_cost_shipping_price',
               'is_free_shipping',
               'inventory_tracking',
               'rating_total',
               'rating_count',
               'total_sold',
               'date_created',
               'brand_id',
               'view_count',
               'page_title',
               'meta_keywords',
               'meta_description',
               'layout_file',
               'is_price_hidden',
               'price_hidden_label',
               'categories',
               'date_modified',
               'event_date_field_name',
               'event_date_type',
               'event_date_start',
               'event_date_end',
               'myob_asset_account',
               'myob_income_account',
               'myob_expense_account',
               'peachtree_gl_account',
               'condition',
               'is_condition_shown',
               'preorder_release_date',
               'is_preorder_only',
               'preorder_message',
               'order_quantity_minimum',
               'order_quantity_maximum',
               'open_graph_type',
               'open_graph_title',
               'open_graph_description',
               'is_open_graph_thumbnail',
               'upc',
               'date_last_imported',
               'option_set_id',
               'tax_class_id',
               'option_set_display',
               'bin_picking_number',
               'custom_url',
               'availability']
	
	a=[col]
	
	data = []
	
	for n in xrange(1,ordercount+1):
		orders = bigcommerce.Products.get(n)
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

a ='/home/mjhabiger/bigcommerce/hist_data/Products%s.txt' % date

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

shutil.copyfile(a,'/home/mjhabiger/bigcommerce/Products.txt') 


		
		
                
	
	
	
	
