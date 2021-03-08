import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from example_plots import plot_oos_status, plot_oos_count, plot_oos_consecutive_order, plot_oos_time_spend

oos_boxes_tab = dac.TabItem(id='content_oos_boxes', 
                              
    children=html.Div(
        [
#            dac.SimpleBox(
#            	style = {'height': "600px"},
#                title = "Box 1",
#                children=[
#                    dcc.Graph(
#			id='box-graph',
#			figure=plot_new_regular(),
#                        config=dict(displayModeBar=False),
#                        style={'width': '38vw'}
#                    )
#                ]
#            ),
            dac.SimpleBox(
            	style = {'height': "600px", 'width':"1100px"},
                title = "OOS position in order status",
                children=[
                    dcc.Graph(
                        figure=plot_oos_status(),
                        config=dict(displayModeBar=False),
                        style={'width': '76vw'}
                    )
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"1100px"},
                title = "Order item attempt and Order item oos",
                children=[
                    dcc.Graph(
                        figure=plot_oos_count(),
                        config=dict(displayModeBar=False),
                        style={'width': '76vw'}
                    )
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"1100px"},
                title = "Consecutive order that user do in same item",
                children=[
                    dcc.Graph(
                        figure=plot_oos_consecutive_order(),
                        config=dict(displayModeBar=False),
                        style={'width': '76vw'}
                    )
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"1100px"},
                title = "User time spend on OOS event",
                children=[
                    dcc.Graph(
                        id='oos-graph',
                        config=dict(displayModeBar=False),
                        style={'width': '76vw'}
                    )
                ]
            )


        ], 
        className='column'
    )
)
