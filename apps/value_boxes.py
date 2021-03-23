import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_scatter, plot_pie, plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus, plot_table_example, plot_table_filter,
plot_voucher_refund_c1, plot_voucher_refund_c2, plot_voucher_refund_c3,
plot_voucher_refund_status)



fig_status, status_count = plot_voucher_refund_status()
fig_c1, c1_count =plot_voucher_refund_c1()
fig_c2, c2_count =plot_voucher_refund_c2()
fig_c3, c3_count =plot_voucher_refund_c3()
value_boxes_tab = dac.TabItem(id='content_value_boxes', 
                              
    children=[
        html.H4('Status order'),
        html.Div([
            dac.ValueBox(
            	value = status_count['Sudah di terima oleh customer'],
              subtitle ='Sudah di terima oleh customer',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Autocancel By System'],
              subtitle = 'Autocancel By System',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Dibatalkan oleh customer care'],
              subtitle = 'Dibatalkan oleh customer care',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Refund'],
              subtitle = 'Refund',
              color = "info",
              icon = "database"
            )
        ], className='row'),
        html.H4('Cases'),
        html.Div([
            dac.InfoBox(
              title = "Success not get voucher",
              value = c1_count,
              icon = "bookmark"
            ),
            dac.InfoBox(
              title = "Delivered but refund",
              color = "info",
              value = c2_count,
              icon = "bookmark"
            ),
            dac.InfoBox(
              title = "Get voucher but not completed",
              gradient_color = "danger",
              value = c3_count,
              icon = "bookmark"
            )
        ], className='row'),
        html.Div([
            dac.SimpleBox(
                # style = {'height': "600px", 'width':"900px"},
                title = "Alfagift SKI order status spread",
                children=[
                    dcc.Graph(
                        figure=fig_status,
                        config=dict(displayModeBar=False),
                        # style={'width': '76vw'}
                    )
                ]
            ),
            dac.SimpleBox(
                # style = {'height': "600px", 'width':"900px"},
                title = "success order but not get voucher",
                children=[
                    fig_c1
                ]
            ),
            dac.SimpleBox(
                # style = {'height': "600px", 'width':"900px"},
                title = "already receive order but submit refund",
                children=[
                    fig_c2
                ]
            ),
            dac.SimpleBox(
                # style = {'height': "600px", 'width':"900px"},
                title = "get voucher but order not completed ",
                children=[
                    fig_c3
                ]
            )
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("75% width card", className="card-title"),
                        html.P(
                            [
                                "This card uses the ",
                                html.Code("w-75"),
                                " class to set the width to 75%",
                            ],
                            className="card-text",
                        ),
                    ]
                ),
                className="w-100 mb-3",
            ),
        ], className='column')
    ]
)