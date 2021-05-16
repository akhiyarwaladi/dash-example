import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_df_m_2802, plot_df_m_3101)
from plots.competitive_plot import plot_product_competitive

fig_, unique_item_ag, change_to_online = plot_df_m_2802()
fig_3101, unique_item_ag_3101, change_to_online_3101 = plot_df_m_3101()

table_product_competitive = plot_product_competitive()

tab_price_compare = dac.TabItem(id='content_price_compare', 
                              
    children=[
        html.Div([
          dbc.Row([
            dbc.Col(

              dac.InfoBox(
                title = "Success delivered but submit refund",
                color = "success",
                value = unique_item_ag,
                icon = "bookmark",
                width = 12
              )
            , md=6),
            dbc.Col(
              dac.InfoBox(
                title = "Get voucher but not success delivered",
                gradient_color = "danger",
                value = change_to_online,
                icon = "bookmark",
                width = 12
              )
            , md=6),
            
          ])
        ]),
        dbc.Row([
          dbc.Col(
            dbc.Card([
              dbc.CardHeader("Detail jan21-feb21"),
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