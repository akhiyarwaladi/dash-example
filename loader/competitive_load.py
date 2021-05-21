import pandas as pd
from helper import transform_format
def get_product_competitive():
	pc = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/product_competitive.csv', sep='\t')

	pc['our_price'] = (pc['our_price'].astype('float')).apply(transform_format)
	pc['comp_price'] = (pc['comp_price'].astype('float')).apply(transform_format)

	n_lower = pc['price_vs'].value_counts().to_dict()[True]
	n_higher = pc['price_vs'].value_counts().to_dict()[True]

	pc['price_vs'] = pc['price_vs'].map({True:'lower', False:'higher'})

	return pc
