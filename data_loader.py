import pandas as pd
import os

parent_path = '/home/server/gli-data-science/akhiyar'

def get_vp():
	vp = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/view_product.csv')
	vp['All'] = vp.sum(axis=1)

	return vp, round(vp.mean(axis=1).mean(), 2), [{'label': x, 'value': x} for x in vp.columns[1:]]
	
def get_sp():
	sp = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/search_product.csv')
	sp['All'] = sp.sum(axis=1)

	return sp, round(sp.mean(axis=1).mean(), 2), [{'label': x, 'value': x} for x in sp.columns[1:]]


def get_cpn():
    campaign_push = pd.read_csv(os.path.join(parent_path, \
                    'out_plot/campaign_push.csv'), sep='\t')
    campaign_push['Campaign Sent Time'] = pd.to_datetime(campaign_push['Campaign Sent Time'])
 
    label = [{'label': x, 'value': x} for x in campaign_push['Campaign Sent Time']\
             .dropna().dt.strftime('%Y-%m').unique()]

    return campaign_push, label

def get_cpe():
    campaign_push = pd.read_csv(os.path.join(parent_path, \
                    'out_plot/campaign_email.csv'), sep='\t')
    campaign_push['Date'] = pd.to_datetime(campaign_push['Date'])
 
    label = [{'label': x, 'value': x} for x in campaign_push['Date']\
             .dropna().dt.strftime('%Y-%m').unique()]

    return campaign_push, label

def get_cpi():
    campaign_push = pd.read_csv(os.path.join(parent_path, \
                    'out_plot/campaign_inapp.csv'), sep='\t')
    campaign_push['Date'] = pd.to_datetime(campaign_push['Date'])
 
    label = [{'label': x, 'value': x} for x in campaign_push['Date']\
             .dropna().dt.strftime('%Y-%m').unique()]

    return campaign_push, label
