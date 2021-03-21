import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash_table
import dash_html_components as html
import datetime


### load example data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = df[['continent', 'country', 'pop', 'lifeExp']]  # prune columns for example
df['Mock Date'] = [
    datetime.datetime(2020, 1, 1, 0, 0, 0) + i * datetime.timedelta(hours=13)
    for i in range(len(df))
]
df_ex = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
###


### place for ski data

res_vcr_oshop_g = pd.read_csv('../../out_plot/voucher_refund/res_vcr_oshop_g.csv', sep='\t')

df_c1 = pd.read_csv('../../out_plot/voucher_refund/c_1.csv', sep='\t')
df_c2 = pd.read_csv('../../out_plot/voucher_refund/c_2.csv', sep='\t')
df_c3 = pd.read_csv('../../out_plot/voucher_refund/c_3.csv', sep='\t')


###

###

df_m_2802 = pd.read_csv('../../df_m_2802.csv', sep='\t')

###




sapa_notsapa = pd.read_csv('../../out_plot/sapa_notsapa.csv', sep='\t')
new_regular = pd.read_csv('../../out_plot/new_regular.csv', sep='\t')
plus_minus = pd.read_csv('../../out_plot/plus_minus.csv', sep='\t')


oos_status = pd.read_csv('../../out_plot/oos_status_spread.csv', sep='\t')
oos_count = pd.read_csv('../../out_plot/order_oos_count.csv', sep='\t')
oos_consecutive_order = pd.read_csv('../../out_plot/consecutive_order_item.csv', sep='\t')
oos_time_spend = pd.read_csv('../../out_plot/time_spend_oos.csv', sep='\t')


plus_minus['diff_sign'] = plus_minus['diff_sign'].astype('str')
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
	fig = px.line(sapa_notsapa, x='tbto_create_date', y='net_amount', template='presentation', \
	              text='tbto_amount_final_rp', color='sapa_enable')
	fig.update_traces(texttemplate='%{text}', textposition='top center', textfont_size=14)
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b\n%Y")
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
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
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_new_regular():
	fig = px.line(new_regular, x='tbto_create_date', y='tbto_amount_final', template='presentation', \
	              text='net_amount', color='member_stat')
	fig.update_traces(texttemplate='%{text}', textposition='top center', textfont_size=14)
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b\n%Y")
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
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
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)	
	
	return fig

def plot_plus_minus():
	fig = px.line(plus_minus, x='wom', y='count_member', template='presentation', \
	              text='count_member', color='diff_sign')
	fig.update_traces(texttemplate='%{text}', textposition='top center', textfont_size=14)
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b\n%Y")
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
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
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_status():
	fig = px.line(oos_status, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2d}', textposition='top center')
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightSteelBlue",
	            bordercolor="Black",
	            borderwidth=2
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_oos_count():
	fig = px.line(oos_count, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2d}', textposition='top center')
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightSteelBlue",
	            bordercolor="Black",
	            borderwidth=2
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_oos_consecutive_order():
	fig = px.line(oos_consecutive_order, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2f}', textposition='top center')
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=0.5,
	            traceorder="reversed",
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightSteelBlue",
	            bordercolor="Black",
	            borderwidth=2
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_time_spend():
	fig = px.line(oos_time_spend, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2f}', textposition='top center')
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightSteelBlue",
	            bordercolor="Black",
	            borderwidth=2
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':20, 't':30, 'b':70},legend=legend_dict)

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
	    plot_df = df[df.WS_DESCRIPTION == r].sort_values('status', ascending=True)
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
	), len(df_m_2802)


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

