import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_view_product1, plot_view_product2)


view_product_tab = dac.TabItem(id='content_view_product', 
                              
    children=[
        html.H4('View Product Event'),

        # html.Div([
        #     dbc.Row([
        #       dbc.Col(
        #         dbc.Card(
        #           [
        #               dbc.CardHeader(""),
        #               dbc.CardBody(
        #                   [
        #                       # html.H5("Card title", className="card-title"),
        #                       html.P(
        #                             plot_view_product1,className="card-text",
        #                       ),
        #                   ]),
        #           ])),
        #       dbc.Col(
        #         dbc.Card(
        #           [
        #               dbc.CardHeader(""),
        #               dbc.CardBody(
        #                   [
        #                       # html.H5("Card title", className="card-title"),
        #                       html.P(
        #                             plot_view_product2,className="card-text",
        #                       ),
        #                   ]),
        #           ])),


        #     ],className="md-12")
        # ], className='column')
    ]
)