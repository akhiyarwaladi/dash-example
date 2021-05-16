import pandas as pd
import dash_table

from competitive_load import get_product_competitive
competitive_table = get_product_competitive()


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
		}
	)