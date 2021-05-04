import pandas as pd

def get_vp():
	vp = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/view_product.csv')
	vp['All'] = vp.sum(axis=1)

	return vp, round(vp.mean(axis=1).mean(), 2), [{'label': x, 'value': x} for x in vp.columns[1:]]
def get_sp():
	sp = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/search_product.csv')
	sp['All'] = sp.sum(axis=1)

	return sp, round(sp.mean(axis=1).mean(), 2), [{'label': x, 'value': x} for x in sp.columns[1:]]
