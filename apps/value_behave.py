import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from example_plots import (plot_scatter, plot_pie, plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus, plot_table_example, plot_table_filter,
plot_voucher_refund_c1, plot_voucher_refund_c2, plot_voucher_refund_c3,
plot_voucher_refund_status, plot_df_m_2802)



fig_status, status_count = plot_voucher_refund_status()
fig_c1, c1_count =plot_voucher_refund_c1()
fig_c2, c2_count =plot_voucher_refund_c2()
fig_c3, c3_count =plot_voucher_refund_c3()


fig_, _count = plot_df_m_2802()

value_behave_tab = dac.TabItem(id='content_value_behave', 
                              
    children=[
        html.H4('Status order'),
        html.Div([
            dac.ValueBox(
            	value = status_count['Sudah di terima oleh customer'],
              subtitle ='Sudah di terima oleh customer',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Autocancel By System'],
              subtitle = 'Autocancel By System',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Dibatalkan oleh customer care'],
              subtitle = 'Dibatalkan oleh customer care',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Refund'],
              subtitle = 'Refund',
              color = "info",
              icon = "database"
            )
        ], className='row'),
        html.Div([

            dac.SimpleBox(
              style = {'height': "600px", 'width':"900px"},
                title = "success order but not get voucher",
                children=[
                    fig_
                ]
            ),
            dac.SimpleBox(
                style = {'height': "600px", 'width':"900px"},
                title = "already receive order but submit refund",
                children=[
                    fig_
                ]
            ),

        ], className='column')
    ]
)