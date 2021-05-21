import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_df_m_2802, plot_df_m_3101)
from plots.competitive_plot import plot_product_competitive
from datetime import datetime
now_str = datetime.now().date().strftime('%d%b')

fig_, unique_item_ag, change_to_online = plot_df_m_2802()
fig_3101, unique_item_ag_3101, change_to_online_3101 = plot_df_m_3101()

product_competitive = plot_product_competitive()
table_product_competitive = product_competitive[0]
lower_price = product_competitive[1]
higher_price = product_competitive[2]


tab_price_compare = dac.TabItem(id='content_price_compare', 
                              
children=[
  html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(html.H4("Product Competitive Price {}".format(now_str))),
                    dbc.CardBody(
                      dbc.Row([
                        dbc.Col(
                          # dac.InfoBox(
                          #   title = "Lower than competitor",
                          #   gradient_color = "success",
                          #   value = lower_price,
                          #   icon = "bookmark",
                          #   width = 16
                          # )
                          card1
                        , width = 3),
                        dbc.Col(
                          # dac.InfoBox(
                          #   title = "Higher than competitor",
                          #   gradient_color = "danger",
                          #   value = higher_price,
                          #   icon = "bookmark",
                          #   width = 16
                          # )
                          card2
                        , width = 3),
                      ], justify="center",)
                    )
                  ]
                ),
              )
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card([
                  dbc.CardHeader(""),
                  dbc.CardBody([
                      # html.H5("Card title", className="card-title"),
                      html.P(
                            table_product_competitive,className="card-text",
                      ),
                  ]),
                ])
              ),
            ]),
  ])
])

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

card1 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 1", className="card-title"),
                    html.P("This card has some text content", className="card-text",),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa fa-list", style=card_icon),
            className="bg-primary",
            style={"maxWidth": 75},
        ),
    ],
    className="mt-4 shadow",
)

card2 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 2", className="card-title"),
                    html.P("This card has some text content", className="card-text",),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa fa-globe", style=card_icon),
            className="bg-info",
            style={"maxWidth": 75},
        ),
    ],className="mt-4 shadow",
)
