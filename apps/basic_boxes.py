import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus)
from datetime import datetime as dt

from dateutil.relativedelta import relativedelta
end_picker = dt.today().date().replace(day=1)
start_picker = end_picker - relativedelta(months=7)


basic_boxes_tab = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div([
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(
                                dbc.Row([
                                    dbc.Col(html.H5("Existing vs New Member Sales"), width=6),

                                    dbc.Col(
                                        html.Div([
                                            html.Div(["DATE: ",
                                            dcc.DatePickerRange(
                                                id='exist_new_picker',
                                                min_date_allowed=dt(2020, 1, 1),
                                                max_date_allowed=dt(2021, 12, 1),
                                                start_date_placeholder_text="Start Date",
                                                end_date_placeholder_text="End Date",
                                                #initial_visible_month=dt(2020, 1, 1),
                                                display_format='DD-MM-Y',
                                                start_date=start_picker,
                                                end_date=end_picker
                                            )],
                                        style={'width': '49%', 'display': 'inline-block'}), 
                                        html.Div(id='output-container-date-picker-range')])
                                    ,width=6),   
                                ],justify="between",),
                            ),

                            dbc.CardBody([
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
                        dbc.Card([
                            dbc.CardHeader(html.H5("Increase and Decrease Sales Member")),
                            dbc.CardBody([
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
