import pandas as pd
import dash_table

from loader.competitive_load import get_product_competitive
from helper import transform_format

product_competitive = get_product_competitive()
competitive_table = product_competitive[0]
lower_price = product_competitive[1]
higher_price = product_competitive[2]

def plot_product_competitive():
	df_init = pd.DataFrame()
	df_init['name'] = list(competitive_table)
	df_init['id'] = list(competitive_table)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=competitive_table.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'minWidth': '50px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		},
		css=[{
		    'selector': '.dash-spreadsheet td div',
		    'rule': '''
		        line-height: 15px;
		        max-height: 30px; min-height: 30px; height: 30px;
		        display: block;
		        overflow-y: hidden;
		    '''
		}],
	    style_cell_conditional=
	    [
	        {
	            'if': {'column_id': c},
	            'textAlign': 'left'
	        } for c in ['product_name_comp', 'url_comp']

	    ] + 
	    [
			{
			    'if': {'column_id': d},
			    'textAlign': 'center'
			} for d in ['plu','our_price','comp_price','price_vs']
		] +
		[
	        {
				'if': {'column_id': 'plu'},
				'width': '80px'
				'fontSize':13
            }
		],
	    style_data_conditional=[
	        {
	            'if': {'row_index': 'odd'},
	            'backgroundColor': 'rgb(248, 248, 248)'
	        },
	        {
	            'if': {
	                'filter_query': '{price_vs} = lower',  # matching rows of a hidden column with the id, `id`
	                'column_id': 'plu'
	            },
	            'backgroundColor': '#3D9970'
	        },
	        {
	            'if': {
	                'filter_query': '{price_vs} = higher',  # matching rows of a hidden column with the id, `id`
	                'column_id': 'plu'
	            },
	            'backgroundColor': '#f55c47'
	        },
	        
	    ],
	    style_header={
	        'backgroundColor': 'rgb(230, 230, 230)',
	        'fontWeight': 'bold', 'fontSize':17, 'font-family':'sans-serif'
	    },

		tooltip_data=[
		    {
		        column: {'value': str(value), 'type': 'markdown'}
		        for column, value in row.items()
		    } for row in competitive_table.to_dict('records')
		],
		tooltip_duration=None
	), lower_price, higher_price