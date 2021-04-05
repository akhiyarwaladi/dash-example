import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_sales_train, plot_sales_test)


fig_sales_train, fig_sales_test = plot_sales_train(), plot_sales_test()

sales_tab = dac.TabItem(id='content_sales', 
                              
    children=[
        html.H4('Status order'),
        html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Fitur apa yang digunakan "),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    'yeay',className="card-text",
                              ),
                          ]),
                  ])),
            ],className="md-12")
        ], className='row'),
        html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Sales training data 01jan20 - 17mar21"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_sales_train,className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Sales prediction 18mar21 - 28mar21"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_sales_test,className="card-text",
                              ),
                          ]),
                  ])),


            ],className="md-12")
        ], className='column')
    ]
)