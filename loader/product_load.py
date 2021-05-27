import pandas as pd

def get_product():
	plu_group = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/product_group.csv',\
		sep='\t')

	return plu_group