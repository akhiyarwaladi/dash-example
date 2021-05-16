import pandas as pd

def get_product_competitive():
	pc = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/product_competitive.csv', sep='\t')


	return pc, p_comp['price_vs'].value_counts().to_dict()[True], p_comp['price_vs'].value_counts().to_dict()[False]
