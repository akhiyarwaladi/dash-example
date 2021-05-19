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

    campaign_push = campaign_push[(campaign_push['Targets'] > 0) \
                            & (campaign_push['Impressions'] > 0)].reset_index(drop=True)
    campaign_push['Conversions_percent'] = round((campaign_push['Conversions'] / campaign_push['Targets']) * 100, 2)
#     campaign_push['Conversions_percent'] = campaign_push['Conversions_percent'].astype(str) + \
#                                             ' ('  + campaign_push['Conversions'].astype(str) + '/' \
#                                             + campaign_push['Targets'].astype(str) + ')'
    
    label = [{'label': x, 'value': x} for x in campaign_push['Campaign Sent Time']\
             .dropna().dt.strftime('%Y-%m').unique()]

    return campaign_push, label

def get_cpe():
    campaign_email = pd.read_csv(os.path.join(parent_path, \
                    'out_plot/campaign_email.csv'), sep='\t')
    campaign_email['Date'] = pd.to_datetime(campaign_email['Date'])
    
    campaign_email = campaign_email[(campaign_email['Targets'] > 0) \
                            & (campaign_email['Impressions'] > 0)].reset_index(drop=True)
    campaign_email['Conversions_percent'] = round((campaign_email['Conversions'] / campaign_email['Targets']) * 100, 2)
#     campaign_email['Conversions_percent'] = campaign_email['Conversions_percent'].astype(str) + \
#                                             ' ('  + campaign_email['Conversions'].astype(str) + '/' \
#                                             + campaign_email['Targets'].astype(str) + ')'

    label = [{'label': x, 'value': x} for x in campaign_email['Date']\
             .dropna().dt.strftime('%Y-%m').unique()]

    return campaign_email, label

def get_cpi():
    campaign_inapp = pd.read_csv(os.path.join(parent_path, \
                    'out_plot/campaign_inapp.csv'), sep='\t')
    campaign_inapp['Date'] = pd.to_datetime(campaign_inapp['Date'])
    campaign_inapp = campaign_inapp[(campaign_inapp['Clicks'] > 0) \
                            & (campaign_inapp['Impressions'] > 0)].reset_index(drop=True)
    
    campaign_inapp['Conversions_percent'] = round((campaign_inapp['Conversions'] / campaign_inapp['Impressions']) * 100, 2)
#     campaign_inapp['Conversions_percent'] = campaign_inapp['Conversions_percent'].astype(str) + \
#                                             ' ('  + campaign_inapp['Conversions'].astype(str) + '/' \
#                                             + campaign_inapp['Impressions'].astype(str) + ')'

    label = [{'label': x, 'value': x} for x in campaign_inapp['Date']\
             .dropna().dt.strftime('%Y-%m').unique()]
    
    return campaign_inapp, label
