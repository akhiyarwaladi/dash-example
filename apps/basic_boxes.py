import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus)
from datetime import datetime as dt



basic_boxes_tab = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(

                        dbc.Row([
                            dbc.Col(html.P('"Existing vs New Member Sales"'), width=4),
                            dbc.Col(html.P('select date range (mm/dd/yyy)'), width=4),
                            dbc.Col(
                                dcc.DatePickerRange(
                                    id='exist_new_picker',
                                    min_date_allowed=dt(2020, 1, 1),
                                    max_date_allowed=dt(2021, 12, 1),
                                    #initial_visible_month=dt(2020, 1, 1),
                                    start_date=dt(2020, 1, 1),
                                    end_date=dt(2021, 12, 1)
                                ),width=4
                            ),   
                        ],justify="start",),


                        ),

                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      id='exist_new_fig',
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),

 
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Increase and Decrease Sales Member"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      id='box-graph',
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),

            ],className="mb-12")
        ], className='column'
    )
)
