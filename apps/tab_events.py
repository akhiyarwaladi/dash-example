import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_general_inapp, plot_order_status)

general_inapp_sel, general_push = plot_general_inapp()
def fill_card_content(header, content):
    card_content = [
        dbc.CardHeader(html.Center(header)),
        dbc.CardBody(
            [
                #html.H5("Card title", className="card-title"),
                html.B(
                    "{} ({}%)".format(content[header],content['%{}'.format(header)]),
                    className="card-title",
                ),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem("Android: {}".format(content['{}_{}'.format('Android',header)])),
                        dbc.ListGroupItem("IOS: {}".format(content['{}_{}'.format('IOS',header)])),

                    ],
                    flush=True,
                ),
            ],
        ),
    ]
    return card_content

def fill_card(header, content, row):
    card_content = [
        dbc.CardHeader(html.H5(header)),
        dbc.CardBody(
            [
              html.H5("Target {} users, goal conversion ({})".format(row['Targets'], \
                row['Primary Conversion Goal']), className="card-title"),
              html.Br(),
              content
            ]
        ),
    ]
    return card_content

li_row = []
for idx, row in general_push.iterrows():
    campaign_name = row['Campaign Name'].strip()
    
    row_x = dbc.Row(
        [

            dbc.Col(dbc.Card(fill_card_content('Impressions', row)\
              , color="dark", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('Clicks', row)\
              , color="dark", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('Conversions', row)\
              , color="dark", outline=True)),

        ],
        className="mb-4",
    )
    row_y = dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                  dbc.CardHeader(html.H5("Alfagift Order Status")),
                  dbc.CardBody(
                      [
                          # html.H5("Card title", className="card-title"),
                          html.P(
                                dcc.Graph(
                                  figure=plot_order_status(),
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                          ),
                      ]),
                ])),
            dbc.Col(dbc.Card(fill_card(campaign_name, row_x, row), color="dark", outline=True)),
        ],
        className="mb-12",
    )
    li_row.append(row_y)

cards = html.Div(li_row)
events_tab = dac.TabItem(id='content_tab_events', 
                              
    children=cards

)