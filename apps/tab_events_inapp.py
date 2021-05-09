import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_general_inapp, conversion_general_inapp, 
                        click_general_inapp)
from plots.campaign_report import g_general_inapp, w_general_inapp
from data_loader import get_cpi

general_inapp = plot_general_inapp()


def fill_card_content(header, content):
    card_content = [
        dbc.CardHeader(html.Center(header)),
        dbc.CardBody(
            [
                #html.H5("Card title", className="card-title"),
                html.B(
                    "{}".format(content[header]),
                    className="card-title",
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
              html.H5("goal conversion ({})".format(\
                row['Conversion Goal']), className="card-title"),
              html.Br(),
              content
            ]
        ),
    ]
    return card_content

li_row = []

row_top = [
        dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                  dbc.CardHeader(html.H5("General In-App Campaign Growth")),
                  dbc.CardBody(
                      [
                          # html.H5("Card title", className="card-title"),
                          html.P(
                                dcc.Graph(
                                  figure=g_general_inapp(get_cpi()[0]),
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                          ),
                      ]),
                ]), md=12),
        ]),
        dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                  
                    dbc.CardHeader(
                      [
                        dbc.Row([
                          dbc.Col(html.Div("Campaign Performance"), md=4),
                          dbc.Col(
                            dcc.Dropdown(
                                id='cpi_dropdown',
                                options=get_cpi()[1],
                                value='2021-04'
                            ), md=4),
                        ], justify='between')
                      ]
                    ),
                  dbc.CardBody(
                      [
                          # html.H5("Card title", className="card-title"),
                          html.P(
                                dcc.Graph(
                                  #figure=w_general_push(campaign_push),
                                  id = 'cpi_fig', 
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                          ),
                      ]),
                ]), md=12),
        ])

]
li_row.append(row_top)


for idx, row in general_inapp.iterrows():
    campaign_name = row['Campaign Name'].strip()
    
    row_x = dbc.Row(
        [

            dbc.Col(dbc.Card(fill_card_content('impressions', row)\
              , color="dark", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('clicks', row)\
              , color="dark", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('conversions (unique)', row)\
              , color="dark", outline=True)),

        ],
        className="mb-4",
    )
    row_y = dbc.Row(
        [
            dbc.Col(dbc.Card(fill_card(campaign_name, row_x, row), color="dark", outline=True)),
        ],
        className="mb-12",
    )
    # li_row.append(row_y)



# li_row = li_row[::-1]

cards = html.Div(li_row)
events_inapp = dac.TabItem(id='content_inapp_events', 
                              
    children=cards

)