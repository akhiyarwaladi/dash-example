import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash_table
import dash_html_components as html
import datetime


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df = df[['continent', 'country', 'pop', 'lifeExp']]  # prune columns for example
df['Mock Date'] = [
    datetime.datetime(2020, 1, 1, 0, 0, 0) + i * datetime.timedelta(hours=13)
    for i in range(len(df))
]




df_ex = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')



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
	fig.update_traces(texttemplate='%{text}', textposition='top center')
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

def plot_new_regular():
	fig = px.line(new_regular, x='tbto_create_date', y='tbto_amount_final', template='presentation', \
	              text='net_amount', color='member_stat')
	fig.update_traces(texttemplate='%{text}', textposition='top center')
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

def plot_plus_minus():
	fig = px.line(plus_minus, x='wom', y='count_member', template='presentation', \
	              text='count_member', color='diff_sign')
	fig.update_traces(texttemplate='%{text}', textposition='top center')
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
	fig.show()

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
	return dash_table.DataTable(
		columns=[
		    {'name': 'Continent', 'id': 'continent', 'type': 'numeric'},
		    {'name': 'Country', 'id': 'country', 'type': 'text'},
		    {'name': 'Population', 'id': 'pop', 'type': 'numeric'},
		    {'name': 'Life Expectancy', 'id': 'lifeExp', 'type': 'numeric'},
		    {'name': 'Mock Dates', 'id': 'Mock Date', 'type': 'datetime'}
		],
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

