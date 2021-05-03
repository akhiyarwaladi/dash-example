import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_view_product1, plot_view_product2, plot_search_product, plot_vp, plot_sp,
  plot_uvp)


view_product_tab = dac.TabItem(id='content_view_product', 
                              
    children=[
        html.H5('View Product Event'),

        html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(""),
                    dbc.CardBody(
                        [
                            html.H5("View product (total event)", className="card-title"),
                            html.P(
                                dcc.Graph(
                                  figure=plot_vp(),
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                            ),
                        ]),
              ]), md=12),
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(""),
                    dbc.CardBody(
                        [
                            html.H5("User view product (total event)", className="card-title"),
                            html.P(
                                dcc.Graph(
                                  figure=plot_uvp(),
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                            ),
                        ]),
              ]), md=12),
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(""),
                    dbc.CardBody(
                        [
                            # html.H5("Card title", className="card-title"),
                            html.P(
                                  plot_view_product1(),className="card-text",
                            ),
                        ]),
              ]), md=12),
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(""),
                    dbc.CardBody(
                        [
                            # html.H5("Card title", className="card-title"),
                            html.P(
                                  plot_view_product2(),className="card-text",
                            ),
                        ]),
              ]), md=12),
            ])
        ]),

        html.H5('Search Product Event'),

        html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(""),
                    dbc.CardBody(
                        [
                            html.H5("Search product (total event)", className="card-title"),
                            html.P(
                                dcc.Graph(
                                  figure=plot_sp(),
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                            ),
                        ]),
              ]), md=12),
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(""),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    plot_search_product(),className="card-text",
                              ),
                          ]),
                  ]), md=12),
            ])
        ])
    ])