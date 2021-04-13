import dash
from dash.dependencies import Input, Output

import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from dash.exceptions import PreventUpdate

# from apps.cards import cards_tab
from apps.social_cards import social_cards_tab
from apps.tab_cards import tab_cards_tab
from apps.basic_boxes import basic_boxes_tab
from apps.general_monitor import general_monitor_tab
from apps.value_boxes import value_boxes_tab
from apps.value_behave import value_behave_tab
from apps.sales import sales_tab
from apps.oos_boxes import oos_boxes_tab

from example_plots import plot_plus_minus, plot_oos_time_spend
from apps.tab_cards import text_1, text_2, text_3

# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = dash.Dash(__name__)
app.title = "Data Science Dashboard"
server = app.server 

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar

right_ui = dac.NavbarDropdown(
	# badge_label = "!",
 #    badge_color= "danger",
 #    src = "https://quantee.ai",
	# header_text="2 Items",
 #    children= [
	# 	dac.NavbarDropdownItem(
	# 		children = "message 1",
	# 		date = "today"
	# 	),
	# 	dac.NavbarDropdownItem(
	# 		children = "message 2",
	# 		date = "yesterday"
	# 	),
	# ]
)
                              
navbar = dac.Navbar(color = "white", 
                    text="Please navigate to one of the sidebar on the left", 
                    children=right_ui)

# Sidebar
subitems = [dac.SidebarMenuSubItem(id='tab_gallery_1', 
                            label='Gallery 1', 
                            icon='arrow-circle-right', 
                            badge_label='Soon',
                            badge_color='success'), 
			dac.SidebarMenuSubItem(id='tab_gallery_2', 
                            label='Gallery 2', 
                            icon='arrow-circle-right', 
                            badge_label='Soon', 
                            badge_color='success')
            ]

# Sidebar
subitems = [dac.SidebarMenuSubItem(id='tab_gallery_3', 
                            label='Gallery 1', 
                            icon='arrow-circle-right', 
                            badge_label='Soon',
                            badge_color='success'), 
            dac.SidebarMenuSubItem(id='tab_gallery_4', 
                            label='Gallery 2', 
                            icon='arrow-circle-right', 
                            badge_label='Soon', 
                            badge_color='success')
            ]

sidebar = dac.Sidebar(
	dac.SidebarMenu(
		[
			#dac.SidebarHeader(children="Cards"),
			#dac.SidebarMenuItem(id='tab_cards', label='Basic cards', icon='box'),
            #dac.SidebarMenuItem(id='tab_social_cards', label='Social cards', icon='id-card'),
            #dac.SidebarMenuItem(id='tab_tab_cards', label='Tab cards', icon='image'),
			dac.SidebarHeader(children="Alfagift"),
            dac.SidebarMenuItem(id='tab_general_monitor', label='General monitor', icon='desktop'),
			dac.SidebarMenuItem(id='tab_basic_boxes', label='Member growth', icon='desktop'),
			dac.SidebarMenuItem(id='tab_oos_boxes', label='Out of stock', icon='desktop'),
			dac.SidebarMenuItem(id='tab_value_boxes', label='Voucher usage', icon='suitcase'),
            dac.SidebarMenuItem(id='tab_value_behave', label='Online-offline compare', icon='suitcase'),
            dac.SidebarMenuItem(id='tab_sales', label='Sales prediction', icon='suitcase'),
            dac.SidebarHeader(children="Member DNA"),
            dac.SidebarMenuItem(label='soon to be updated ...', icon='cubes', children=subitems),
			dac.SidebarHeader(children="Gallery"),
			dac.SidebarMenuItem(label='soon to be updated ...', icon='cubes', children=subitems),
		]
	),
    title='Data Science Dashboard',
	skin="light",
    color="primary",
	brand_color="primary",
    url="",
    src="",
    elevation=3,
    opacity=0.8
)

# Body
body = dac.Body(
    dac.TabItems([
        #cards_tab,
        #social_cards_tab,
        #tab_cards_tab,
        general_monitor_tab,
        basic_boxes_tab,
        oos_boxes_tab,
        value_boxes_tab,
        value_behave_tab,
        sales_tab,
        dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'), 
                    id='content_gallery_1'),
        dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'), 
                    id='content_gallery_2'),
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title = "My right sidebar",
    skin = "light"
)

# Footer
footer = dac.Footer(
	html.A("@Global Loyalty Indonesia",
		href = "", 
		target = "_blank", 
	),
	right_text = "2021"
)

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

# =============================================================================
# Callbacks
# =============================================================================
def activate(input_id, 
             n_general_monitor, n_basic_boxes, n_oos_boxes, n_value_boxes, n_value_behave,
             n_sales, n_gallery_1, n_gallery_2):
    
    # Depending on tab which triggered a callback, show/hide contents of app
    if input_id == 'tab_general_monitor' and n_general_monitor:
        return True, False, False, False, False, False, False, False
    elif input_id == 'tab_basic_boxes' and n_basic_boxes:
        return False, True, False, False, False, False, False, False
    elif input_id == 'tab_oos_boxes' and n_oos_boxes:
        return False, False, True, False, False, False, False, False
    elif input_id == 'tab_value_boxes' and n_value_boxes:
        return False, False, False, True, False, False, False, False
    elif input_id == 'tab_value_behave' and n_value_behave:
        return False, False, False, False, True, False, False, False
    elif input_id == 'tab_sales' and n_sales:
        return False, False, False, False, False, True, False, False       
    elif input_id == 'tab_gallery_1' and n_gallery_1:
        return False, False, False, False, False, False, True, False
    elif input_id == 'tab_gallery_2' and n_gallery_2:
        return False, False, False, False, False, False, False, True
    # initialization
    else:
        return True, False, False, False, False, False, False, False
    
@app.callback([Output('content_general_monitor', 'active'),
               Output('content_basic_boxes', 'active'),
               Output('content_oos_boxes', 'active'),
               Output('content_value_boxes', 'active'),
               Output('content_value_behave', 'active'),
               Output('content_sales', 'active'),
               Output('content_gallery_1', 'active'),
               Output('content_gallery_2', 'active')],
               [Input('tab_general_monitor', 'n_clicks'),
                Input('tab_basic_boxes', 'n_clicks'),
                Input('tab_oos_boxes', 'n_clicks'),
                Input('tab_value_boxes', 'n_clicks'),
                Input('tab_value_behave', 'n_clicks'),
                Input('tab_sales', 'n_clicks'),
                Input('tab_gallery_1', 'n_clicks'),
                Input('tab_gallery_2', 'n_clicks')]
)

def display_tab(n_general_monitor, n_basic_boxes, n_oos_boxes, n_value_boxes, n_value_behave, 
                n_sales, n_gallery_1, n_gallery_2):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]   

    return activate(input_id, 
                    n_general_monitor, n_basic_boxes, n_oos_boxes, n_value_boxes, n_value_behave, 
                    n_sales, n_gallery_1, n_gallery_2)

@app.callback([Output('tab_general_monitor', 'active'),
               Output('tab_basic_boxes', 'active'),
               Output('tab_oos_boxes', 'active'),
               Output('tab_value_boxes', 'active'),
               Output('tab_value_behave', 'active'),
               Output('tab_sales', 'active'),
               Output('tab_gallery_1', 'active'),
               Output('tab_gallery_2', 'active')],
               [Input('tab_general_monitor', 'n_clicks'),
                Input('tab_basic_boxes', 'n_clicks'),
                Input('tab_oos_boxes', 'n_clicks'),
                Input('tab_value_boxes', 'n_clicks'),
                Input('tab_value_behave', 'n_clicks'),
                Input('tab_sales', 'n_clicks'),
                Input('tab_gallery_1', 'n_clicks'),
                Input('tab_gallery_2', 'n_clicks')]
)

def activate_tab(n_general_monitor, n_basic_boxes, n_oos_boxes, n_value_boxes, n_value_behave, 
                n_sales, n_gallery_1, n_gallery_2):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0] 

    return activate(input_id, 
                    n_general_monitor, n_basic_boxes, n_oos_boxes, n_value_boxes, n_value_behave, 
                    n_sales, n_gallery_1, n_gallery_2)
    



# @app.callback(Output('tab_box_1', 'children'),
#               [Input('tab_box_1_menu', 'active_tab')]
# )
# def display_tabbox1(active_tab):

#     # Depending on tab which triggered a callback, show/hide contents of app
#     if active_tab == 'tab_box_1_tab1':
#         return text_1
#     elif active_tab == 'tab_box_1_tab2':
#         return text_2
#     elif active_tab == 'tab_box_1_tab3':
#         return text_3

# @app.callback(Output('tab_box_2', 'children'),
#               [Input('tab_box_2_menu', 'active_tab')]
# )
# def display_tabbox2(active_tab):

#     # Depending on tab which triggered a callback, show/hide contents of app
#     if active_tab == 'tab_box_2_tab1':
#         return text_1
#     elif active_tab == 'tab_box_2_tab2':
#         return text_2
#     elif active_tab == 'tab_box_2_tab3':
#         return text_3


# Update figure on slider change
@app.callback(
    Output('box-graph', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    return plot_plus_minus()
    

# Update figure on slider change
@app.callback(
    Output('oos-graph', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_oos_graph(value):
    return plot_oos_time_spend()
    


# =============================================================================
# Run app    
# =============================================================================
if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', debug=True)
