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
    fig = px.bar(g_push_wide_s, y="Campaign Name", x=["Targets", "Impressions", "Clicks", "Conversions"], \
                    orientation='h', title="Wide-Form Input")
    fig.update_traces(
        hovertemplate='%{x}')

    fig.update_layout(font={'size': 16}, width=1000,template='presentation',
                    plot_bgcolor = '#FFFFFF',height=700,
                    xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
                           'showgrid': True, 'automargin': True, 'title':'Campaign'},
                    yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
                           'showgrid': True,  'automargin': True, 'title':'#Event'},
                    bargap=0.7, title="Campaign push notif performance {}".format(value), title_x=0.5)

    
    return fig


def g_general_inapp(campaign_inapp):
    g_inapp = campaign_inapp.groupby([pd.Grouper(key='Date',freq='M')])\
            .agg({'Impressions':'sum', 'Clicks':'sum', 'Conversions':'sum'}).reset_index()

    g_inapp['Date'] = g_inapp['Date'].dt.strftime('%Y-%m')
    g_inapp = pd.melt(g_inapp, ['Date'])

    g_inapp['value_format'] = g_inapp['value'].astype('float').apply(transform_to_format)
    fig = px.line(g_inapp, x='Date', y='value', template='presentation', \
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

def w_general_inapp(campaign_inapp, value):
    g_inapp_wide = campaign_inapp.groupby([pd.Grouper(key='Date',freq='M'), 'Campaign Name'])\
           .agg({'Impressions':'sum', 'Clicks':'sum', 'Conversions':'sum'}).reset_index()
    g_inapp_wide['Date'] = g_inapp_wide['Date'].dt.strftime('%Y-%m')
    g_inapp_wide = g_inapp_wide[g_inapp_wide['Date'] == value]

    # g_push_wide_s['Campaign Name'] = pd.Series(split_label(g_push_wide_s['Campaign Name'].str[10:]))
    fig = px.bar(g_inapp_wide, y="Campaign Name", x=["Impressions", "Clicks", "Conversions"], \
                orientation='h', title="Wide-Form Input")
    fig.update_traces(
        hovertemplate='%{x}')
    fig.update_layout(font={'size': 16}, width=1000,template='presentation',
                    plot_bgcolor = '#FFFFFF',height=700,
                    xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
                           'showgrid': True, 'automargin': True, 'title':'Campaign'},
                    yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
                           'showgrid': True,  'automargin': True, 'title':'#Event'},
                    bargap=0.3, title="Campaign inapp performance {}".format(value), title_x=0.5)

    
    return fig


def g_general_email(campaign_email):
    g_email = campaign_email.groupby([pd.Grouper(key='Date',freq='M')])\
            .agg({'Targets':'sum', 'Impressions':'sum', 'Clicks':'sum', 'Conversions':'sum'}).reset_index()

    g_email['Date'] = g_email['Date'].dt.strftime('%Y-%m')
    g_email = pd.melt(g_email, ['Date'])

    g_email['value_format'] = g_email['value'].astype('float').apply(transform_to_format)
    fig = px.line(g_email, x='Date', y='value', template='presentation', \
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

def w_general_email(campaign_email, value):
    g_email_wide = campaign_email.groupby([pd.Grouper(key='Date',freq='M'), 'Campaign Name'])\
           .agg({'Targets':'sum', 'Impressions':'sum', 'Clicks':'sum', 'Conversions':'sum'}).reset_index()
    g_email_wide['Date'] = g_email_wide['Date'].dt.strftime('%Y-%m')
    g_email_wide = g_email_wide[g_email_wide['Date'] == value]

    # g_push_wide_s['Campaign Name'] = pd.Series(split_label(g_push_wide_s['Campaign Name'].str[10:]))
    fig = px.bar(g_email_wide, y="Campaign Name", x=["Targets", "Impressions", "Clicks"], \
                orientation='h', title="Wide-Form Input")
    fig.update_traces(
        hovertemplate='%{x}')
    fig.update_layout(font={'size': 16}, width=1000,template='presentation',
                    plot_bgcolor = '#FFFFFF',height=700,
                    xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
                           'showgrid': True, 'automargin': True, 'title':'Campaign'},
                    yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
                           'showgrid': True,  'automargin': True, 'title':'#Event'},
                    bargap=0.3, title="Campaign email performance {}".format(value), title_x=0.5)

    
    return fig