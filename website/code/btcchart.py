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
    return '<br><b>' + primary_label + '</b></br>Day: %{x|%Y-%m-%d}<br>' + primary_value_description + ': %{y:,.2f} ' + primary_val_unit + '<extra></extra>'

def get_value_chart_desc(primary_label: DataFrame, secondary_value_description: str, seconday_val_unit: str, currency: str):

    if currency.upper() == 'BTC':
        prec = ': %{y:,.8f} '
    elif currency == '%':
        prec = ': %{y:,.4f} '
    else:
        prec = ': %{y:,.2f} '

    return '<br><b>' + primary_label + '</b></br>Day: %{x|%Y-%m-%d}<br>' + secondary_value_description + prec + seconday_val_unit + '<extra></extra>'


def get_range(chart_range) -> dict:
    return {
        "legend": True,
        "scales": dict(
                        rangeselector=dict(
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
                        ),
                        rangeslider=dict(
                            visible=True
                        ),
                        rangeslider_thickness = 0.06,
                        type="date",
                        fixedrange=False,
                        range=chart_range
                      )
    } 


def get_chart_params(chart_type: str, primaryDF, secondaryDF, primary_val_label, seconday_val_label, seconday_val_unit) -> dict:
    if chart_type == 'log':
        ctick=1
        frange=[-1.2, max(primaryDF[primary_val_label])*0.8/10000]
        srange=[-1.2, max(primaryDF[primary_val_label])*0.8/10000]
        #crange=None
    else:
        ctick=None
        frange=None
        srange=None

        if seconday_val_unit == '%':
            ctick=10
            srange=[0,max(secondaryDF[seconday_val_label]) * 1.01]
    
    return {'ctick': ctick, 'srange': srange, 'frange': frange}


def get_main_chart():
    return make_subplots(specs=[[{"secondary_y": True}]])

def add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, is_secondary = False):
    fig.add_trace(
                        go.Scattergl(x = primaryDF['day'], 
                                     y = primaryDF[primary_val_label], 
                                     name = primary_label,
                                     line = dict(color=PRICE_CHART_PROPERTIES['COLOR']),
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
        currency = currency.upper() if currency != None and currency != "" else "BTC"
        chart_range = get_range(range) if show_full else {'legend': False, 'scales': None}
        chart_params = get_chart_params(secondary_type, primaryDF, secondaryDF, primary_val_label, seconday_val_label, seconday_val_unit)


        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit)
        fig = add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)

        if show_full:
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
            xaxis=dict(
                rangeslider=dict(visible=False if show_full == False else True, thickness=0.1, bgcolor="#191a1d"),
                #chart_range['scales']
                showgrid=False if show_full == False else True,
                tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                gridcolor="#1e1f22"
            ),
            yaxis=dict( #price
                            title=primary_label,
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
                            fixedrange = False if show_full == False else True,
                            range=chart_params['frange'],
                            gridcolor="#1e1f22"
                        ),
            yaxis2=dict( ##chart
                            title=secondary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            type=secondary_type,
                            showgrid=True,
                            fixedrange = False if show_full == False else True,
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

        chart_range = get_range(None)
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
        
          

        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, True)
        fig = add_cross_pointer_to_chart(fig)   
        fig = add_halvings_to_chart(fig, primaryDF)

        fig.update_layout(
            font_family=PROPERTY_CHART_DEFAULT_FONT,
            template=PROPERTY_CHART_DEFAULT_STYLE,
            height=PROPERTY_CHART_DEFAULT_HEIGHT,
            showlegend=chart_range['legend'],
            legend=dict(yanchor="bottom", y=-0.30, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=50, b=10),
            yaxis=dict(
                            title=secondary_chart_name,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            range=[0,100],
                            fixedrange=False
                        ),
            yaxis2=dict(
                            title=primary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=True,
                            type="log",
                            dtick = 1,
                            fixedrange=False
                        ),
            xaxis=chart_range['scales']
                       
            
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


        chart_range = get_range(None) if show_full else {'legend': False, 'scales': None}
        
        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, False)
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
            font_family="Arial",
            template="simple_white",
            height=height,
            showlegend=False,
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title=primary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=False,
                            type="log",
                            dtick = 1,
                            fixedrange = False
                        ),
            yaxis2=dict(
                            title=secondary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            fixedrange = False,
                            showgrid=True,
                            range=[min(valsList)*0.98, max(valsList)*1.02]
                        )
        )
        

        fig.add_hline(y=1, line_width=1,  line_color="black", line_dash="dash", secondary_y=True, opacity=1)

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
        chart_range = get_range(range) if show_full else {'legend': False, 'scales': None}
        chart_params = get_chart_params(secondary_chart_type, primaryDF, secondaryDF, primary_val_label, seconday_val_label, seconday_val_unit)


        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, False)
        fig = add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label)
        fig = add_halvings_to_chart(fig, primaryDF)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)
    
        fig.update_layout(
            font_family="Arial",
            template="simple_white",
            height=height,
            width=width,
            showlegend=chart_range['legend'],
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title=primary_label,
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
                            range=chart_params['frange']
                        ),
            yaxis2=dict(
                            title=secondary_label,
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            type=secondary_chart_type,
                            fixedrange = False,
                            dtick = chart_params['ctick'],
                            range=chart_params['srange']
                        )
        )
        
        

        fig.add_hrect(y0=76, y1=100, line_width=0, line_dash="dash", line_color="black", fillcolor="#ff5f46", opacity=0.2, secondary_y=True)
        fig.add_hline(y=76, line_width=1, line_dash="dot", line_color="#C68484", secondary_y=True, opacity=0.5)

        fig.add_hrect(y0=51, y1=75.99, line_width=0, line_dash="dash", line_color="black", fillcolor="#f3b229", opacity=0.2, secondary_y=True)
        fig.add_hline(y=51, line_width=1, line_dash="dot", line_color="#f3b229", secondary_y=True, opacity=0.5)

        fig.add_hrect(y0=25, y1=50.99, line_width=0, line_dash="dash", line_color="black", fillcolor="#ffd772", opacity=0.1, secondary_y=True)
        fig.add_hline(y=25, line_width=1, line_dash="dot", line_color="#ffc005", secondary_y=True, opacity=0.5)

        fig.add_hrect(y0=-170, y1=0, line_width=0, line_dash="dash", line_color="#000000", fillcolor="#0D6E6E", opacity=0.2, secondary_y=True)
        fig.add_hline(y=0, line_width=1, line_dash="dot", line_color="#0D6E6E", secondary_y=True, opacity=0.5)


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


        chart_range = get_range(None) if show_full else {'legend': False, 'scales': None}
        currency = "BTC"
        fill_label = "LINE"

        fig = get_main_chart()
        fig = add_price_to_chart(fig, primaryDF, primary_label, primary_val_label, primary_value_description, primary_val_unit, False)
        fig = add_value_to_chart(fig, secondaryDF, secondary_label, seconday_val_label, secondary_value_description, seconday_val_unit, currency, fill_label, True)
        fig = add_image_to_chart(fig)
        fig = add_cross_pointer_to_chart(fig)
        fig = add_halvings_to_chart(fig, primaryDF)


        
        fig.update_layout(
            font_family="Arial",
            template="simple_white",
            height=height,
            width=width,
            showlegend=chart_range['legend'],
            legend=dict(yanchor="bottom", y=-0.25, xanchor="center", x=0.46, orientation="h"),
            margin=dict(l=0, r=0, t=40, b=10),
            xaxis=chart_range['scales'],
            yaxis=dict(
                            title="Price of BTC (USD)",
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=False,
                            type="log",
                            dtick = 1,
                            fixedrange = False
                        ),
            yaxis2=dict(
                            title="MVRV Z-Score",
                            titlefont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            tickfont=dict(
                                color=PROPERTY_CHART_SIDE_TITLE_COLOR
                            ),
                            showgrid=True,
                            fixedrange = False
                        )
        )
        

        fig.add_hrect(y0=11, y1=18, line_width=0, line_dash="dash", line_color="black", fillcolor="#ff5f46", opacity=0.1, secondary_y=True)
        fig.add_hrect(y0=-0.4, y1=0.7, line_width=0, line_dash="dash", line_color="#000000", fillcolor="#0D6E6E", opacity=0.1, secondary_y=True)
        fig.add_hline(y=11, line_width=1,  line_color="#C68484", secondary_y=True, opacity=0.5)
        fig.add_hline(y=0.7, line_width=1,  line_color="#50727B", secondary_y=True, opacity=0.5)
        fig.add_hline(y=-0.4, line_width=1,  line_color="#50727B", secondary_y=True, opacity=0.5)


        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)