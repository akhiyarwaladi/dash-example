import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_general_inapp)



general_inapp_sel = plot_general_inapp()
def fill_card_content(header, content):
    card_content = [
        dbc.CardHeader(header),
        dbc.CardBody(
            [
                #html.H5("Card title", className="card-title"),
                html.P(
                    content,
                    className="card-text",
                ),
            ]
        ),
    ]
    return card_content

def fill_card(header, content):
    card_content = [
        dbc.CardHeader(header),
        dbc.CardBody(
            [
              'content'
            ]
        ),
    ]
    return card_content

li_row = []
for idx, row in general_inapp_sel.iterrows():
    campaign_name = row['Campaign Name'].strip()
    print(campaign_name)
    row_x = dbc.Row(
        [
          dbc.Row([
            dbc.Col(dbc.Card(fill_card(campaign_name, [
            dbc.Col(dbc.Card(fill_card_content('impressions', row['impressions']), color="primary", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('clicks', row['clicks']), color="primary", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('closed', row['closed']), color="primary", outline=True)),
            ]), color="primary", outline=True)
            )
            
          ],
          className="mb-12",
          )
        ],
        className="mb-4",
    )
    li_row.append(row_x)

cards = html.Div(li_row)


events_tab = dac.TabItem(id='content_tab_events', 
                              
    children=cards

)