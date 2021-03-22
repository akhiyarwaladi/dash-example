import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from example_plots import (plot_scatter, plot_pie, plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus, plot_table_example, plot_table_filter,
plot_voucher_refund_c1, plot_voucher_refund_c2, plot_voucher_refund_c3,
plot_voucher_refund_status, plot_df_m_2802)


fig_, unique_item_ag, change_to_online = plot_df_m_2802()

value_behave_tab = dac.TabItem(id='content_value_behave', 
                              
    children=[
        html.H4('Status order'),
        html.Div([
            dac.ValueBox(
            	value = unique_item_ag,
              subtitle ='Number of user always buy different item on alfagift transaction',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = change_to_online,
              subtitle = 'Number of user change their item buy from offline to online',
              color = "info",
              icon = "database"
            ),
        ], className='row'),
        html.Div([

            dac.SimpleBox(
              style = {'height': "600px", 'width':"900px"},
                title = "Detail jan21-feb21",
                children=[
                    fig_
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "Detail dec20-jan21",
                children=[
                    fig_
                ]
            ),

        ], className='column')
    ]
)