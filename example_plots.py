import numpy as np 
import pandas as pd
import os
import textwrap

import plotly.express as px
import plotly.graph_objs as go
import dash_table
import dash_html_components as html
import datetime
from datetime import date, timedelta


def split_label(list_label):
    list_label = list(list_label)
    list_label = ["<br>".join(textwrap.wrap(t, width=8)) for t in list_label ]
    return list_label


### load example data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = df[['continent', 'country', 'pop', 'lifeExp']]  # prune columns for example
df['Mock Date'] = [
    datetime.datetime(2020, 1, 1, 0, 0, 0) + i * datetime.timedelta(hours=13)
    for i in range(len(df))
]
df_ex = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
###

parent_path = '/home/server/gli-data-science/akhiyar'
### place for ski data

res_vcr_oshop_g = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/res_vcr_oshop_g.csv'), sep='\t')

df_c1 = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/c_1.csv'), sep='\t')
df_c2 = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/c_2.csv'), sep='\t')
df_c3 = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/c_3.csv'), sep='\t')

###

###

df_m_2802 = pd.read_csv(os.path.join(parent_path, 'out_plot/df_m_2802.csv'), sep='\t')
df_m_3101 = pd.read_csv(os.path.join(parent_path, 'out_plot/df_m_3101.csv'), sep='\t')

###
## member monitoring
sapa_notsapa = pd.read_csv(os.path.join(parent_path, 'out_plot/sapa_notsapa.csv'), sep='\t')
new_regular = pd.read_csv(os.path.join(parent_path, 'out_plot/new_regular.csv'), sep='\t')
plus_minus = pd.read_csv(os.path.join(parent_path, 'out_plot/plus_minus.csv'), sep='\t')
plus_minus = pd.concat([pd.DataFrame([['2020-10','decrease sales','0','Rp 0'],['2020-10','increase sales','0','Rp 0']],\
            columns=list(plus_minus)),plus_minus])

oos_status = pd.read_csv(os.path.join(parent_path, 'out_plot/oos_status_spread.csv'), sep='\t')
oos_count = pd.read_csv(os.path.join(parent_path, 'out_plot/order_oos_count.csv'), sep='\t')
oos_consecutive_order = pd.read_csv(os.path.join(parent_path, 'out_plot/consecutive_order_item.csv'), sep='\t')
oos_time_spend = pd.read_csv(os.path.join(parent_path, 'out_plot/time_spend_oos.csv'), sep='\t')


oos_status['month'] = pd.to_datetime(oos_status['month']).dt.strftime('%b%y')
oos_count['month'] = pd.to_datetime(oos_count['month']).dt.strftime('%b%y')
oos_consecutive_order['month'] = pd.to_datetime(oos_consecutive_order['month']).dt.strftime('%b%y')
oos_time_spend['month'] = pd.to_datetime(oos_time_spend['month']).dt.strftime('%b%y')

###
res_g = pd.read_csv(os.path.join(parent_path, 'out_plot/res_g.csv'), sep='\t')
all_df_pred = pd.read_csv(os.path.join(parent_path, 'out_plot/all_df_pred.csv'), sep='\t')



res_unstack = res_g.set_index(["TRO_DATE", "DESCP_DEPT"])['TRO_NET'].unstack(level=1).fillna(0)
pred_unstack = all_df_pred.set_index(["TRO_DATE", "DESCP_DEPT"])['TRO_NET'].unstack(level=1).fillna(0)



###

def multi_plot(df, addAll = True):
    fig = go.Figure()

    for column in df.columns.to_list():

        fig.add_trace(
            go.Scatter(
                x = df.index,
                y = df[column],
                name = column
            )
        )

    button_all = dict(label = 'All',
                      method = 'update',
                      args = [{'visible': df.columns.isin(df.columns),
                               'title': 'All',
                               'showlegend':True}])

    def create_layout_button(column):
        return dict(label = column,
                    method = 'update',
                    args = [{'visible': df.columns.isin([column,column]),
                             'title': column,
                             'showlegend': True}])

    fig.update_layout(
        updatemenus=[go.layout.Updatemenu(
            active = 0,
            buttons = ([button_all] * addAll) + list(df.columns.map(lambda column: create_layout_button(column))),
            x = 0.3,
            xanchor = 'left',
            y = 1.2,
            yanchor = 'top',
            )
        ], template='presentation')
    
    return fig


def plot_sales_train():
	return multi_plot(res_unstack)

def plot_sales_test():
	return multi_plot(pred_unstack)



def plot_pie():
    
    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500,2000,1053,500]
    colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']
    
    trace = go.Pie(labels=labels, values=values,
                   hoverinfo='label+percent', textinfo='value', 
                   textfont=dict(size=20),
                   marker=dict(colors=colors, 
                               line=dict(color='#000000', width=2)))
                                         
    return dict(data=[trace]) 

def plot_sapa_notsapa():
	
	sapa_notsapa['sapa_enable'] = sapa_notsapa['sapa_enable'].replace({'not_sapa':'non_sapa'})
	fig = px.line(sapa_notsapa, x='tbto_create_date', y='net_amount', template='presentation', \
	              text='tbto_amount_final_rp', color='sapa_enable')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_new_regular():
	new_regular['member_stat'] = new_regular['member_stat'].replace({'regular':'existing'})
	fig = px.line(new_regular, x='tbto_create_date', y='tbto_amount_final', template='presentation', \
	              text='net_amount', color='member_stat')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='net_amount'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	
	return fig

def plot_plus_minus():

	fig = px.line(plus_minus, x='date', y='count_member', template='presentation', \
	                color='diff_sign', text='count_member')

	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{y}')
	for ix, trace in enumerate(fig.data):
	    if ix == 1:
	        trace.update(textposition='bottom center')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=2
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_status():

	fig = px.line(oos_status, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2d}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%Y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#trx'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_count():


	fig = px.line(oos_count, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2d}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#attempt'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_oos_consecutive_order():
	fig = px.line(oos_consecutive_order, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2f}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%Y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#order'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_time_spend():
	
	fig = px.line(oos_time_spend, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%Y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='how long'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig


def plot_table_example():
	fig = go.Figure(data=[go.Table(
	    header=dict(values=list(df_ex.columns),
	                fill_color='LightSteelBlue',
	                align='left'),
	    cells=dict(values=[df_ex.Rank, df_ex.State, df_ex.Postal, df_ex.Population],
	               fill_color='lavender',
	               align='left'))
	])

	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':20, 't':30, 'b':70},template='presentation')
	return fig

def plot_table_filter():
	df_init = pd.DataFrame()
	df_init['name'] = list(df)
	df_init['id'] = list(df)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(
		columns=columns,
		data=df.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	)


def plot_voucher_refund_status():
	df = res_vcr_oshop_g.copy()
	df['WS_DESCRIPTION'] = pd.Series(split_label(df['WS_DESCRIPTION']))
	df['tbtpp_name'] = pd.Series(split_label(df['tbtpp_name']))
	
	period_upper = date.today()
	period_lower = (period_upper - timedelta(days=5)) 
	period_upper = period_upper.strftime('%Y-%m-%d')
	period_lower = period_lower.strftime('%Y-%m-%d')

	df = df[(df['tbto_create_date'] >= period_lower) \
			& (df['tbto_create_date'] <= period_upper)]

	fig = go.Figure()

	fig.update_layout(
	    template="presentation",
	    xaxis=dict(title_text="Week"),
	    yaxis=dict(title_text="Count"),
	    barmode="stack",
	)

	colors = ["#B6E2D3", "#e4bad4", '#E7D2CC', '#FFA384', '#D6AD60', '#18A558']
	colors = colors[0:len(df.WS_DESCRIPTION.unique())]
	for r, c in zip(df.WS_DESCRIPTION.unique(), colors):
	    plot_df = df[df.WS_DESCRIPTION == r]
	    #display(plot_df)
	    fig.add_trace(
	        go.Bar(x=[plot_df.tbto_create_date, plot_df.tbtpp_name], y=plot_df.status, \
	               name=r, marker_color=c),
	    )

	status_count = res_vcr_oshop_g.groupby('WS_DESCRIPTION').agg({'status':'sum'}).to_dict()['status']
	return fig, status_count


def plot_voucher_refund_c1():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_c1)
	df_init['id'] = list(df_c1)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=df_c1.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), len(df_c1)
def plot_voucher_refund_c2():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_c2)
	df_init['id'] = list(df_c2)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=df_c2.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), len(df_c2)
def plot_voucher_refund_c3():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_c3)
	df_init['id'] = list(df_c3)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=df_c3.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), len(df_c3)


def plot_df_m_2802():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_m_2802)
	df_init['id'] = list(df_m_2802)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	unique_item_ag = df_m_2802[df_m_2802['m_item_ag_len'] > 0].shape[0]
	change_to_online = df_m_2802[df_m_2802['m_online_len'] > 0].shape[0]
	return dash_table.DataTable(


		columns=columns,
		data=df_m_2802.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), unique_item_ag, change_to_online

def plot_df_m_3101():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_m_3101)
	df_init['id'] = list(df_m_3101)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	unique_item_ag = df_m_3101[df_m_3101['m_item_ag_len'] > 0].shape[0]
	change_to_online = df_m_3101[df_m_3101['m_online_len'] > 0].shape[0]
	return dash_table.DataTable(


		columns=columns,
		data=df_m_3101.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), unique_item_ag, change_to_online	


def plot_scatter(N=50):
    
    trace1 = go.Scatter(
        y = np.random.randn(N),
        mode='markers',
        marker=dict(
            size=16,
            color = np.random.randn(N), #set color equal to a variable
            colorscale='Viridis',
            showscale=True
        )
    )
        
    return dict(data=[trace1])

def plot_surface():
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    
    data = [
        go.Surface(
            z=z_data.values,
            contours=go.surface.Contours(
                z=go.surface.contours.Z(
                  show=True,
                  usecolormap=True,
                  highlightcolor="#42f462",
                  project=dict(z=True)
                )
            )
        )
    ]
    layout = go.Layout(
        title='Mt Bruno Elevation',
        scene=dict(camera=dict(eye=dict(x=1.87, y=0.88, z=-0.64))),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(
            l=35,
            r=20,
            b=35,
            t=45
        )
    )
    return go.Figure(data=data, layout=layout)

