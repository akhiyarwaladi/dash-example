import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from example_plots import (plot_scatter, plot_pie, plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus, plot_table_example)



basic_boxes_tab = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div(
        [

            dac.SimpleBox(
            	style = {'height': "600px", 'width':"900px"},
                title = "SAPA vs non SAPA store sales",
                children=[
                    dcc.Graph(
                        figure=plot_sapa_notsapa(),
                        config=dict(displayModeBar=False),
                        style={'width': '72vw'}
                    )
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "New vs Regular member sales",
                children=[
                    dcc.Graph(
                        figure=plot_new_regular(),
                        config=dict(displayModeBar=False),
                        style={'width': '72vw'}
                    )
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "Up and Down sales member",
                children=[
                    dcc.Graph(
                        id='box-graph',
                        config=dict(displayModeBar=False),
                        style={'width': '72vw'}
                    )
                ]
            )


        ], 
        className='column'
    )
)
