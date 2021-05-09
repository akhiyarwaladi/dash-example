import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

import os
import textwrap

import dash_table
import dash_html_components as html

from datetime import date, timedelta, datetime
from helper import transform_to_rupiah_format,transform_to_format,transform_format


def g_general_push(campaign_push):
    g_push = campaign_push.groupby([pd.Grouper(key='Campaign Sent Time',freq='M')])\
            .agg({'Targets':'sum', 'Impressions':'sum', 'Clicks':'sum', 'Conversions':'sum'}).reset_index()

    g_push['Campaign Sent Time'] = g_push['Campaign Sent Time'].dt.strftime('%Y-%m')
    g_push = pd.melt(g_push, ['Campaign Sent Time'])

    g_push['value_format'] = g_push['value'].astype('float').apply(transform_to_format)
    fig = px.line(g_push, x='Campaign Sent Time', y='value', template='presentation', \
                  text='value_format', color='variable')
    fig.update_traces(texttemplate='%{text}', 
        textposition='top center', 
        textfont_size=11,
        hovertemplate='%{x}<br>%{text}')
    for ix, trace in enumerate(fig.data):
        if ix == 3:
            trace.update(textposition='bottom center')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b%y",
        showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
    )
    fig.update_yaxes(

        showgrid=True, gridwidth=1, gridcolor='LightPink', title='#'
    )

    legend_dict = \
        legend=dict(
                x=0,
                y=1,
                traceorder="normal",
                title='',
                title_font_family="Times New Roman",
                font=dict(
                    family="Courier",
                    size=12,
                    color="black"
                ),
                bgcolor="LightGrey",
                bordercolor="Black",
                borderwidth=1
            )
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
                      {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

    return fig

def w_general_push(campaign_push, value):
    g_push_wide = campaign_push.groupby([pd.Grouper(key='Campaign Sent Time',freq='M'), 'Campaign Name'])\
           .agg({'Targets':'sum', 'Impressions':'sum', 'Clicks':'sum', 'Conversions':'sum'}).reset_index()
    g_push_wide['Campaign Sent Time'] = g_push_wide['Campaign Sent Time'].dt.strftime('%Y-%m')
    g_push_wide_s = g_push_wide[g_push_wide['Campaign Sent Time'] == value]

    # g_push_wide_s['Campaign Name'] = pd.Series(split_label(g_push_wide_s['Campaign Name'].str[10:]))
    fig = px.bar(g_push_wide_s, x="Campaign Name", y=["Targets", "Impressions", "Clicks", "Conversions"], title="Wide-Form Input")

    fig.update_layout(font={'size': 16}, width=1000,template='presentation',
                    plot_bgcolor = '#FFFFFF',
                    xaxis={'showline': True, 'visible': True, 'showticklabels': False, \
                           'showgrid': True, 'automargin': True, 'title':'Campaign'},
                    yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
                           'showgrid': True,  'automargin': True, 'title':'#Event'},
                    bargap=0.3, title="Campaign push notif performance {}".format(value), title_x=0.5)

    
    return fig