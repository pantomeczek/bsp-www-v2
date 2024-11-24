from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import plotly.graph_objects as go
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import timedelta, datetime
from .constants import *
from pandas.core.frame import DataFrame 


def get_date_as_string(dt, mask = '%Y-%m-%d'):
    return dt.strftime(mask)

def get_string_as_date(str):
    return  datetime.strptime(str,'%Y-%m-%d')


def get_price_chart_desc(primary_label: str, primary_value_description: str, primary_val_unit: str):
    return '<br><b>' + primary_label + '</b></br>Day: %{x|%Y-%m-%d}<br>' + primary_value_description + ': %{y:,.2f} ' + primary_val_unit +'<extra></extra>'

def get_value_chart_desc(primary_label: DataFrame, secondary_value_description: str, seconday_val_unit: str, currency: str):

    
    if currency.upper() == 'BTC':
        prec = ': %{y:,.8f} '
    elif currency == '%':
        prec = ': %{y:,.4f} '
    else:
        prec = currency + ': %{y:,.2f} '

    return '<br><b>' + primary_label + '</b></br>Day: %{x|%Y-%m-%d}<br>' + secondary_value_description + prec + seconday_val_unit + '<extra></extra>'


def get_range(chart_range, show_full = True) -> dict:

    if show_full:
        rs = dict(
                            bgcolor="#212529",  # Background color
                            activecolor="#57585a",  # Active button color
                            font=dict(color="white"),
                            buttons=list([
                                dict(count=1,
                                    label="1m",
                                    step="month",
                                    stepmode="backward"),
                                dict(count=6,
                                    label="6m",
                                    step="month",
                                    stepmode="backward"),
                                dict(count=1,
                                    label="YTD",
                                    step="year",
                                    stepmode="todate"),
                                dict(count=1,
                                    label="1y",
                                    step="year",
                                    stepmode="backward"),
                                dict(count=3,
                                    label="3y",
                                    step="year",
                                    stepmode="backward"),
                                dict(step="all")
                            ])
                        )
    else:
        rs = None

    return {
        "legend": False if show_full == False else True,
        "scales": dict(
                        rangeselector=rs,
                        rangeslider=dict(visible=False if show_full == False else True, thickness=0.1, bgcolor="#191a1d"),
                        showgrid=False if show_full == False else True,
                        tickfont=dict(
                                        color=PROPERTY_CHART_SIDE_TITLE_COLOR
                                    ),
                        gridcolor="#1e1f22",
                        rangeslider_thickness = 0.06,
                        type="date",
                        fixedrange=False,
                        range=chart_range
                      )
    } 


def get_chart_params(chart_type: str, primaryDF, secondaryDF, primary_val_label, seconday_val_label, seconday_val_unit, show_full = False) -> dict:
    if chart_type == 'log':
        ctick=1
        frange=[min(primaryDF[primary_val_label])*1.13/10000, max(primaryDF[primary_val_label])*0.5/10000]
        srange=[min(primaryDF[primary_val_label])*1.13/10000, max(primaryDF[primary_val_label])*0.5/10000]
        #crange=None
    else:
        ctick=None
        frange=None
        srange=[min(secondaryDF[seconday_val_label]), max(secondaryDF[seconday_val_label])] if show_full == False else None

        if seconday_val_unit == '%':
            ctick=10
            srange=[0,max(secondaryDF[seconday_val_label]) * 1.01]
    
    return {'ctick': ctick, 'srange': srange, 'frange': frange}


def get_main_chart():
    return make_subplots(specs=[[{"secondary_y": True}]])

def add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, is_secondary = False, price_color = PRICE_CHART_PROPERTIES['COLOR']):
    fig.add_trace(
                        go.Scattergl(x = primaryDF['day'], 
                                     y = primaryDF[primary_val_label], 
                                     name = primary_label,
                                     line = dict(color=price_color),
                                     line_width = PRICE_CHART_PROPERTIES['LINE_WEIGHT'],
                                     hovertemplate = get_price_chart_desc(primary_label, primary_value_description, primary_val_unit),
                                     hoverlabel=dict(
                                                        bgcolor=PRICE_CHART_PROPERTIES['COLOR'],  # Background color
                                                        bordercolor=PRICE_CHART_PROPERTIES['COLOR'],    # Border color
                                                        font=dict(
                                                            color="#191a1d",   # Font color
                                                            size=11            # Font size
                                                        )
                                                    )
                                    ),
                                    secondary_y = is_secondary
                )


    return fig

def add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label, is_secondary = True):
    fig.add_trace(
                        go.Scatter(
                                    x = secondaryDF['day'], 
                                    y = secondaryDF[seconday_val_label], 
                                    name = secondary_label,
                                    line = dict(color = VALUE_CHART_PROPERTIES[currency][fill_label]['line']),
                                    fillcolor = VALUE_CHART_PROPERTIES[currency][fill_label]['fill'],
                                    line_width = VALUE_CHART_PROPERTIES[currency][fill_label]['weight'],
                                    fill = VALUE_CHART_PROPERTIES[currency][fill_label]['fill_mode'],
                                    hovertemplate = get_value_chart_desc(secondary_label, secondary_value_description, seconday_val_unit, currency),
                                    hoverlabel=dict(
                                                        bgcolor=VALUE_CHART_PROPERTIES[currency][fill_label]['line'],  # Background color
                                                        bordercolor=VALUE_CHART_PROPERTIES[currency][fill_label]['line'],    # Border color
                                                        font=dict(
                                                            color="#191a1d",   # Font color
                                                            size=11            # Font size
                                                        )
                                                    )
                                  ),
                                  secondary_y=is_secondary
                    )
    return fig

def add_image_to_chart(fig):
    fig.add_layout_image(dict(
                                source="/static/img/background_logo.png",
                                xref="paper", 
                                yref="paper",
                                x=0, 
                                y=1,
                                sizex=1, 
                                sizey=1,
                                xanchor="left",
                                yanchor="top",
                                sizing="contain",
                                layer="below",
                                opacity=0.12
                            )
                        )
    return fig
    
def add_cross_pointer_to_chart(fig):
    fig.update_xaxes(showspikes=True,
                     spikecolor="grey",
                     spikesnap="cursor",
                     spikemode="across",
                     spikedash="dash",
                     spikethickness=1
                    )
    fig.update_yaxes(showspikes=True,
                     spikecolor="grey",
                     spikesnap="cursor",
                     spikemode="across",
                     spikedash="dash",
                     spikethickness=1
                    )
    
    return fig

def add_titles_to_chart(fig, primary_label, secondary_label):
    fig.update_yaxes(title_text=primary_label, secondary_y=False)
    fig.update_yaxes(title_text=secondary_label, secondary_y=True)

    return fig

def add_halvings_to_chart(fig, primaryDF):

    halvings = ["2012-11-28", "2016-07-09", "2020-05-11", "2024-04-20"]

    for h in halvings:
        if primaryDF[primaryDF['day'] == h].shape[0] > 0:
            fig.add_vline(x=h, line_width=1, line_dash="dash", line_color="#464748")

    return fig

def get_color_for_value(value):
    rv = None
    try:
        if value < 1:
            rv = "#ff5f46"
        else:
            rv = "#0D6E6E"
    except:
        rv = 'pink'

    return rv



def get_daily_chart(primaryDF: DataFrame, 
                    secondaryDF: DataFrame, 
                    primary_val_label: str, 
                    seconday_val_label: str, 
                    primary_val_unit: str, 
                    seconday_val_unit: str, 
                    primary_label: str,
                    secondary_label: str,
                    primary_value_description: str,
                    secondary_value_description: str,
                    fillunder: bool,
                    currency: str,
                    range,
                    height: int,
                    width: int,
                    show_full: bool,
                    secondary_type: str):

        
        fill_label = "FILL" if fillunder else "LINE"
        currency = currency.upper() if currency != None and currency != "" else ""
        chart_range = get_range(range, show_full) 
        chart_params = get_chart_params(secondary_type, primaryDF, secondaryDF, primary_val_label, seconday_val_label, seconday_val_unit, show_full)

        

        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit)
        fig = add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)


        

        #chart_params = {'ctick': 1, 'srange': [4, 7.949131939431674], 'frange': [4, 7.949131939431674]}

        if show_full:
            fig = add_halvings_to_chart(fig, primaryDF)

        fig.update_layout(
            font_family=PROPERTY_CHART_DEFAULT_FONT,
            template=PROPERTY_CHART_DEFAULT_STYLE,
            plot_bgcolor='#16171a',
            paper_bgcolor='#16171a',
            height=height,
            width=width,
            dragmode=False if show_full == False else "zoom",
            showlegend=chart_range['legend'],
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict( #price
                            title="" if show_full == False else primary_label ,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=False,
                            type="log",
                            dtick = 0.1 if show_full == False else 1,
                            tickformat="$,f",
                            fixedrange = False ,
                            range=chart_params['frange'],
                            gridcolor="#1e1f22"
                        ),
            yaxis2=dict( ##chart
                            title="" if show_full == False else secondary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            type=secondary_type,
                            showgrid=True,
                            fixedrange = False ,
                            dtick = chart_params['ctick'],
                            range=chart_params['srange'],
                            gridcolor="#1e1f22"
                        )
        )
        
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def get_special_comparison_chart(primaryDF, 
                                 listOfDFs,
                                 primary_val_label, 
                                 seconday_val_label, 
                                 primary_val_unit, 
                                 primary_label,
                                 primary_value_description,
                                 secondary_chart_name,
                                 fill):

        chart_range = get_range(None, True) 
        fig = get_main_chart()

    
        for key, val in listOfDFs.items():
            fig.add_trace(
                            go.Scatter(
                                        x=val['df']['day'], y=val['df'][seconday_val_label],
                                        name=val["name"],
                                        opacity=1,
                                        hoverinfo='x+y',
                                        mode='lines',
                                        hovertemplate = '<br><b>' + val["label"] + '</b></br>Day: %{x|%Y-%m-%d}<br>' + val["description"] + ': %{y:,.2f} ' + val["unit"] + '<extra></extra>',
                                        line=dict(width=0.5, color=val["color"]),
                                        fillcolor = val["color"],
                                        stackgroup='one' # define stack group
                                       ), 
                            secondary_y=False
                        )
        
          

        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, True, '#000')
        fig = add_cross_pointer_to_chart(fig)   
        fig = add_halvings_to_chart(fig, primaryDF)

        fig.update_layout(
            font_family=PROPERTY_CHART_DEFAULT_FONT,
            template=PROPERTY_CHART_DEFAULT_STYLE,
            height=PROPERTY_CHART_DEFAULT_HEIGHT,
            plot_bgcolor='#16171a',
            paper_bgcolor='#16171a',
            showlegend=chart_range['legend'],
            legend=dict(yanchor="bottom", y=-0.30, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=50, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title= "" if show_full == False else secondary_chart_name,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            range=[0,100],
                            fixedrange=False,
                            gridcolor="#1e1f22"
                        ),
            yaxis2=dict(
                            title= "" if show_full == False else primary_label ,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=True,
                            type="log",
                            dtick = 1,
                            fixedrange=False,
                            gridcolor="#1e1f22"
                        )
                       
            
        ) 

        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)



def get_sopr_chart(primaryDF: DataFrame, 
                   secondaryDF: DataFrame, 
                   primary_val_label: str, 
                   seconday_val_label: str, 
                   primary_val_unit: str, 
                   seconday_val_unit: str, 
                   primary_label: str,
                   secondary_label: str,
                   primary_value_description: str,
                   secondary_value_description: str,
                   height: int,
                   show_full: bool):


        chart_range = get_range(None, show_full) 
        
        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, False)
        if show_full:
            fig = add_halvings_to_chart(fig, primaryDF)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)
       
        new_colors = []


        for val in secondaryDF['calculated_value']:
            elem = ""
            if val > 0.99 and val < 1:
                elem = '#9B4444'
            elif val >= 1.01:
                elem = '#5D9C59'
            elif val <= 0.99:
                elem = "#9B4444"
            else:
                elem = "#5D9C59"

            new_colors.append(elem)


        tmp_df, valsList = [], []
        last_val, last_day = None, None;
        last_color = "grey"
    

        for index, row in secondaryDF.iterrows():
            
            day = row['day']
            val = row['calculated_value']

            if not pd.isnull(row['calculated_value']):
                valsList.append(float(row['calculated_value']))
            
            if last_val == None: #first time
                tmp_df.append({'day': row['day'], 'calculated_value': val}) 
                last_val = val
                last_day = day
                last_color = get_color_for_value(val)
            else:
                if get_color_for_value(val) == get_color_for_value(last_val): #if same as before then just add
                    tmp_df.append({'day': row['day'], 'calculated_value': val}) 
                    last_val = val
                    last_day = day
                    last_color = get_color_for_value(val)
                else:

                    tmp_df[-1] = {'day': last_day, 'calculated_value': 1}

                    tmpPdDF = pd.DataFrame(tmp_df).sort_values(by=['day'])
                    
                    
                    
                    fig.add_trace(
                                    go.Scatter(
                                        x=tmpPdDF['day'],
                                        y=tmpPdDF['calculated_value'], 
                                        mode='lines', 
                                        line={'color': get_color_for_value(last_val)},
                                        hovertemplate = get_value_chart_desc(secondary_label, "SOPR Value", "", "")
                                    ),secondary_y=True
                                 )
                    tmpPdDF=None
                    tmp_df = []
                    tmp_df.append({'day': last_day, 'calculated_value': 1}) 
                    tmp_df.append({'day': row['day'], 'calculated_value': val}) 
                    last_val = val
                    last_day = day
        
        if tmp_df != None and len(tmp_df) > 0:
            tmpPdDF = pd.DataFrame(tmp_df).sort_values(by=['day'])
            fig.add_trace(
                            go.Scatter(
                                x=tmpPdDF['day'],
                                y=tmpPdDF['calculated_value'], 
                                mode='lines', 
                                line={'color': get_color_for_value(last_val)},
                                hovertemplate = get_value_chart_desc(secondary_label, "SOPR Value", "", "")
                            ),secondary_y=True
                            )   

            

        fig.update_layout(
            font_family=PROPERTY_CHART_DEFAULT_FONT,
            template=PROPERTY_CHART_DEFAULT_STYLE,
            plot_bgcolor='#16171a',
            paper_bgcolor='#16171a',
            height=height,
            showlegend=False,
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title="" if show_full == False else primary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=False,
                            type="log",
                            dtick = 1,
                            fixedrange = False,
                            gridcolor="#1e1f22"
                        ),
            yaxis2=dict(
                            title="" if show_full == False else secondary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            fixedrange = False,
                            showgrid=True,
                            range=[min(valsList)*0.98, max(valsList)*1.02],
                            gridcolor="#1e1f22"
                        )
        )
        

        fig.add_hline(y=1, line_width=1,  line_color="#57585a", line_dash="dash", secondary_y=True, opacity=1)

        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def get_nupl_chart(primaryDF, 
                   secondaryDF, 
                   primary_val_label, 
                   seconday_val_label, 
                   primary_val_unit, 
                   seconday_val_unit, 
                   primary_label,
                   secondary_label,
                   primary_value_description,
                   secondary_value_description,
                   fillunder,
                   currency,
                   range,
                   height,
                   width,
                   show_full,
                   secondary_chart_type):

        fill_label = "FILL" if fillunder else "LINE"
        currency = currency.upper() if currency != None and currency != "" else "BTC"
        chart_range = get_range(range, show_full) 
        chart_params = get_chart_params(secondary_chart_type, primaryDF, secondaryDF, primary_val_label, seconday_val_label, seconday_val_unit)


        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, False)
        fig = add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label)
        fig = add_halvings_to_chart(fig, primaryDF)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)
    
        fig.update_layout(
            font_family=PROPERTY_CHART_DEFAULT_FONT,
            template=PROPERTY_CHART_DEFAULT_STYLE,
            plot_bgcolor='#16171a',
            paper_bgcolor='#16171a',
            width=width,
            height=height,
            showlegend=False,
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title="" if show_full == False else primary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=True,
                            type="log",
                            dtick = 1,
                            fixedrange = False,
                            range=chart_params['frange'],
                            gridcolor="#1e1f22"
                        ),
            yaxis2=dict(
                            title="" if show_full == False else secondary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            type=secondary_chart_type,
                            fixedrange = False,
                            showgrid=False,
                            dtick = chart_params['ctick'],
                            range=chart_params['srange'],
                            gridcolor="#1e1f22"
                        )
        )
        
        

        fig.add_hrect(y0=7.6, y1=100, line_width=0, line_dash="dash", line_color="black", fillcolor="#d12004", opacity=0.2, secondary_y=True)
        fig.add_hline(y=7.6, line_width=1, line_dash="solid", line_color="#d12004", secondary_y=True, opacity=0.2)

        fig.add_hrect(y0=5.1, y1=75.99, line_width=0, line_dash="dash", line_color="black", fillcolor="#fa8b41", opacity=0.07, secondary_y=True)
        fig.add_hline(y=5.1, line_width=1, line_dash="solid", line_color="#fa8b41", secondary_y=True, opacity=0.2)

        fig.add_hrect(y0=-17.0, y1=0, line_width=0, line_dash="dash", line_color="#000000", fillcolor="#569468", opacity=0.07, secondary_y=True)
        fig.add_hline(y=0, line_width=1, line_dash="solid", line_color="#569468", secondary_y=True, opacity=0.2)


        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def get_mvrv_chart(primaryDF, 
                   secondaryDF, 
                   primary_val_label, 
                   seconday_val_label, 
                   primary_val_unit, 
                   seconday_val_unit, 
                   primary_label,
                   secondary_label,
                   primary_value_description,
                   secondary_value_description,
                   width = None, 
                   height = 800, 
                   show_full = True):


        chart_range = get_range(None, show_full) 
        currency = "BTC"
        fill_label = "LINE"

        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, False)
        fig = add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label, True)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)
        fig = add_halvings_to_chart(fig, primaryDF)


        
        fig.update_layout(
            font_family=PROPERTY_CHART_DEFAULT_FONT,
            template=PROPERTY_CHART_DEFAULT_STYLE,
            plot_bgcolor='#16171a',
            paper_bgcolor='#16171a',
            height=height,
            width=width,
            showlegend=chart_range['legend'],
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title="" if show_full == False else "Price of BTC (USD)",
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=False,
                            type="log",
                            dtick = 1,
                            fixedrange = False,
                            gridcolor="#1e1f22"
                        ),
            yaxis2=dict(
                            title="" if show_full == False else "MVRV Z-Score",
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=True,
                            fixedrange = False,
                            gridcolor="#1e1f22"
                        )
        )
        

        fig.add_hrect(y0=11, y1=18, line_width=0, line_dash="dash", line_color="black", fillcolor="#d12004", opacity=0.07, secondary_y=True)
        fig.add_hrect(y0=-0.4, y1=0.7, line_width=0, line_dash="dash", line_color="#000000", fillcolor="#569468", opacity=0.07, secondary_y=True)
        
        fig.add_hline(y=11, line_width=1,  line_color="#C68484", secondary_y=True, opacity=0.5)
        fig.add_hline(y=0.7, line_width=1,  line_color="#50727B", secondary_y=True, opacity=0.5)
        fig.add_hline(y=-0.4, line_width=1,  line_color="#50727B", secondary_y=True, opacity=0.5)


        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def get_pie_chart(height, data, data_type):
    labels = data['headers']
    values = data['data']

    if data_type == 'percent':
        textinfo = 'value'
        hoverinfo='label+value'
    
    else:
        textinfo = 'percent'
        hoverinfo='label+value+percent'
    

    fig = get_main_chart()
    show_full = False
    chart_range = get_range(None, show_full) 

    fig = go.Figure(
        data=[go.Pie(labels=labels, 
                     values=values, 
                     hole=0.6,
                     textinfo=textinfo,  # Show labels and raw percentage values
                     hoverinfo=hoverinfo,
                     textposition='inside', 
                     textfont=dict(
                        family=PROPERTY_CHART_DEFAULT_FONT,        # Font family
                        size=12,               # Font size
                        color='white',         # Font color
                        weight='bold'          # Bold text
                     ),
                     marker=dict(
                                  colors=['rgba(247, 148, 51,  .85)', 
                                          'rgba(169, 76, 104,  .85)', 
                                          'rgba(226, 133, 113, .85)', 
                                          'rgba(248, 204, 146, .85)', 
                                          'rgba(170, 214, 184, .85)', 
                                          'rgba(133, 188, 190, .85)',
                                          'rgba(109, 151, 195, .85)',
                                          'rgba(124, 117, 178, .85)'
                                          ],
                                  line=dict(color='#16171a', width=3)
                                )
                    )]  # hole=0.0 creates a regular pie chart
    )

    # Update layout (optional)
    

    fig.update_layout(
                        font_family=PROPERTY_CHART_DEFAULT_FONT,
                        template=PROPERTY_CHART_DEFAULT_STYLE,
                        plot_bgcolor='#16171a',
                        paper_bgcolor='#16171a',
                        height=height,
                        showlegend=True,
                        legend=dict(
                                        x=0.5,            # Place the legend at the left edge (0 means the leftmost position)
                                        xanchor="center",  # Align the left side of the legend box to the x position
                                        y=-0.2,          # Vertically center the legend (50% of the plot height)
                                        yanchor="bottom", # Align the center of the legend box to the y position
                                        orientation="h"
                                    ),
                        margin=dict(l=0, r=0, t=40, b=10),
                    )

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

     