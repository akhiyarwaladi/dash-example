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
		    'width': '120px', 'minWidth': '120px', 'maxWidth': '150px',
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
	    style_cell_conditional=[
	        {
	            'if': {'column_id': c},
	            'textAlign': 'left'
	        } for c in ['product_name_comp', 'url_comp', 'price_vs']
	    ],
	    style_data_conditional=[
	        {
	            'if': {'row_index': 'odd'},
	            'backgroundColor': 'rgb(248, 248, 248)'
	        }
	    ],
	    style_header={
	        'backgroundColor': 'rgb(230, 230, 230)',
	        'fontWeight': 'bold'
	    }
	), lower_price, higher_price