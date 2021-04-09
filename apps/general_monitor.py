import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_store_type_sales, plot_new_regular)



general_monitor_tab = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("SAPA vs non-SAPA Store Sales"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_store_type_sales(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Existing vs New Member Sales"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_new_regular(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),


            ],className="mb-12")
        ], className='column'
    )
)
