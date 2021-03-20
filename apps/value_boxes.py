import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from example_plots import (plot_scatter, plot_pie, plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus, plot_table_example, plot_table_filter,
plot_voucher_refund_c1, plot_voucher_refund_c2, plot_voucher_refund_c3,
plot_voucher_refund_status)



fig_status, status_count = plot_voucher_refund_status()
value_boxes_tab = dac.TabItem(id='content_value_boxes', 
                              
    children=[
        html.H4('Value Boxes'),
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
        html.H4('Info Boxes'),
        html.Div([
            dac.InfoBox(
              title = "Messages",
              value = 1410,
              icon = "envelope"
            ),
            dac.InfoBox(
              title = "Bookmarks",
              color = "info",
              value = 240,
              icon = "bookmark"
            ),
            dac.InfoBox(
              title = "Comments",
              gradient_color = "danger",
              value = 41410,
              icon = "comments"
            )
        ], className='row'),
        html.Div([
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "Alfagift SKI order status spread",
                children=[
                    dcc.Graph(
                        figure=fig_status,
                        config=dict(displayModeBar=False),
                        style={'width': '76vw'}
                    )
                ]
            ),
            dac.SimpleBox(
              style = {'height': "600px", 'width':"900px"},
                title = "success order but not get voucher",
                children=[
                    plot_voucher_refund_c1()
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "already receive order but submit refund",
                children=[
                    plot_voucher_refund_c2()
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "get voucher but order not completed ",
                children=[
                    plot_voucher_refund_c3()
                ]
            )
        ], className='column')
    ]
)