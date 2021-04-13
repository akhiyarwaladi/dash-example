import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus)



basic_boxes_tab = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div([
            dbc.Row([
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
                      dbc.CardFooter(
                          dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=dt(2019, 1, 1),
                            max_date_allowed=dt(2019, 1, 4),
                            initial_visible_month=dt(2019, 1, 1),
                            end_date=dt(2019, 1, 4)
                          ),


                        ),
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
