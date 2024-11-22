from flask import Flask, render_template
from . import btcchart
from .constants import *
from .postgresql_connection import PostgresConn
import pandas as pd
from pandas.core.frame import DataFrame 
from datetime import timedelta, datetime

def get_df_from_query(query, columns, conn = None) -> DataFrame:
 
     cn = PostgresConn() if conn == None else conn

     session = cn.get_cursor_to_pg()       
     session.execute(query)
     result = session.fetchall()
     resultDF = pd.DataFrame(result, columns=columns)

     if conn == None:
          cn.close_connection()

     return resultDF

def get_range(priceDF, holdingsDF) -> list:
     new_dt = holdingsDF['day'].min() - pd.Timedelta(days=90)

     if new_dt < priceDF['day'].min():
          new_dt = priceDF['day'].min()

     return [new_dt, priceDF['day'].max()]


def get_values_in_usd(priceDF, holdingsDF) -> DataFrame:

     usdDF = []
        
     for index, row in holdingsDF.iterrows():

          day = row['day'].date()
          val = row['calculated_value']
          day2 = row['day'].date().strftime('%Y-%m-%d')
          try:
               price = float((priceDF.query(f"day == '{day2}'")[PROPERTY_PRICE_CHART_VALUE_COLUMN]).iloc[0])
               calc_val = round(val * price,2)
               usdDF.append({'day': row['day'], PROPERTY_VALUE_CHART_VALUE_COLUMN: calc_val})
          except:
               pass
     
     return pd.DataFrame(usdDF, columns=['day',PROPERTY_VALUE_CHART_VALUE_COLUMN]).sort_values(by=['day'])

def get_indicators_perc_details(days_back, sql_query, columns, details_dict, indicator_prefix, indicator_suffix):
     addrDF = get_df_from_query(sql_query, columns)

     lastDay = addrDF['day'].max()
     prevDay = lastDay - timedelta(days=days_back)

     lastDf = addrDF[addrDF.day == lastDay]
     prevDf = addrDF[addrDF.day == prevDay]

     addDetailsList = details_dict

     for i in addDetailsList:
          try:
               addDetailsList[i]['current_percentage'] = round(lastDf.loc[lastDf.indicator_name == indicator_prefix + i + indicator_suffix, 'calculated_value'].values[0],2)
          except:
               addDetailsList[i]['current_percentage'] = 0
          try:  
               addDetailsList[i]['previous_percentage'] = round(prevDf.loc[prevDf.indicator_name == indicator_prefix + i + indicator_suffix, 'calculated_value'].values[0],2)
          except:
               addDetailsList[i]['previous_percentage'] = 0

          addDetailsList[i]['diff'] = round(addDetailsList[i]['current_percentage'] - addDetailsList[i]['previous_percentage'], 2)
          addDetailsList[i]['change'] = 'minus' if addDetailsList[i]['current_percentage'] < addDetailsList[i]['previous_percentage']  else 'plus' if addDetailsList[i]['current_percentage'] > addDetailsList[i]['previous_percentage'] else 'none'


     return addDetailsList

def get_standard_price_chart(indicator_name: str, 
                             indicator_title: str, 
                             indicator_value_label: str, 
                             indicator_value_unit: str, 
                             filled: bool = False, 
                             chart_date_from: str = PROPERTY_CHARTS_DEFAULT_VALID_FROM, 
                             chart_currency: str = PROPERTY_BTC_CODE, 
                             limited_range: bool = False, 
                             chart_height: int = 900, 
                             chart_width: int = None, 
                             show_all_tools: bool = True,
                             secondary_chart_type: str = None):

     cn = PostgresConn() 
     
     priceDF = get_df_from_query(f"select day, calculated_value as value \
                                     from public.general_indicator \
                                    where indicator_name = 'bitcoin_price' \
                                      and day >= to_date('{chart_date_from}', 'YYYY-MM-DD') \
                                    order by day asc", 
                                 ['day','value'], 
                                 cn)

     holdingsDF = get_df_from_query(f"select day, calculated_value \
                                        from general_indicator \
                                       where indicator_name='{indicator_name}' \
                                         and day >= to_date('{chart_date_from}', 'YYYY-MM-DD') \
                                       order by day asc", 
                                    ['day','calculated_value'], 
                                    cn)

     cn.close_connection()

     chart_range = get_range(priceDF, holdingsDF) if limited_range else None   
     holdingsDF  = get_values_in_usd(priceDF, holdingsDF) if chart_currency.upper() == PROPERTY_USD_CODE else holdingsDF   
           

     graph = btcchart.get_daily_chart(priceDF, 
                                      holdingsDF, 
                                      PROPERTY_PRICE_CHART_VALUE_COLUMN, 
                                      PROPERTY_VALUE_CHART_VALUE_COLUMN, 
                                      PROPERTY_PRICE_SIGN,
                                      indicator_value_unit,
                                      PROPERTY_PRICE_CHART_TITLE, 
                                      indicator_title, 
                                      PROPERTY_PRICE_CHART_LABEL, 
                                      indicator_value_label, 
                                      filled,
                                      chart_currency,
                                      chart_range,
                                      chart_height,
                                      chart_width,
                                      show_all_tools,
                                      secondary_chart_type)
       
          
     return graph


def get_special_address_price_chart():
            
     cn = PostgresConn() 
     priceDF     = get_df_from_query(f"select day, calculated_value as value from general_indicator where indicator_name = 'bitcoin_price' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD') order by day asc", ['day','value'], cn)
     planktonDF  = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='plankton_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     shrimpsDF   = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='shrimps_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     crabsDF     = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='crabs_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     fishDF      = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='fish_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     sharksDF    = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='sharks_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     whalesDF    = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='whales_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     humpbacksDF = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='humpbacks_percentage' and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)
     cn.close_connection()

     listDF = {
               "plankton": {
                    "df": planktonDF,
                    "name": "Plankton (less then 0.01)",
                    "color": "#a94c68",
                    "label": "% of total supply - Plankton",
                    "description": "Value",
                    "unit": "%"
               },
               "shrimps": {
                    "df": shrimpsDF,
                    "name": "Shrimps (0.01 to 1)",
                    "color": "#e28571",
                    "label": "% of total supply - Shrimps",
                    "description": "Value",
                    "unit": "%"
               },
               "crabs": {
                    "df": crabsDF,
                    "name": "Crabs (1 to 10)",
                    "color": "#f8cc92",
                    "label": "% of total supply - Crabs",
                    "description": "Value",
                    "unit": "%"
               },
               "fish": {
                    "df": fishDF,
                    "name": "Fish (10 to 100)",
                    "color": "#aad6b8",
                    "label": "% of total supply - Fish",
                    "description": "Value",
                    "unit": "%"
               },
               "sharks": {
                    "df": sharksDF,
                    "name": "Sharks (100 to 1,000)",
                    "color": "#85bcbe",
                    "label": "% of total supply - Sharks",
                    "description": "Value",
                    "unit": "%"
               },
               "whales": {
                    "df": whalesDF,
                    "name": "Whales (1,000 to 10,000)",
                    "color": "#6d97c3",
                    "label": "% of total supply - Whales",
                    "description": "Value",
                    "unit": "%"
               },
               "humpbacks": {
                    "df": humpbacksDF,
                    "name": "Humpbacks (more then 10,000)",
                    "color": "#7c75b2",
                    "label": "% of total supply - Humpbacks",
                    "description": "Value",
                    "unit": "%"
               }           
        }


     graph = btcchart.get_special_comparison_chart(priceDF, 
                                                  listDF,
                                                  PROPERTY_PRICE_CHART_VALUE_COLUMN, 
                                                  PROPERTY_VALUE_CHART_VALUE_COLUMN, 
                                                  PROPERTY_PRICE_SIGN,
                                                  PROPERTY_PRICE_CHART_TITLE, 
                                                  PROPERTY_PRICE_CHART_LABEL, 
                                                  'Coins Distribution (% of total supply)',
                                                  None)

     return graph

def get_nupl_chart( indicator, 
                    label, 
                    metric_label, 
                    metric_unit, 
                    filled = None, 
                    date_from = "2010-07-01", 
                    chart_currency = "BTC", 
                    limited_range = None, 
                    height = 900, 
                    width = None, 
                    show_full = True,
                    secondary_chart_type = None):

     cn = PostgresConn() 
     priceDF = get_df_from_query(f"select day, calculated_value as value from general_indicator where indicator_name = 'bitcoin_price' and day >= to_date('{date_from}', 'YYYY-MM-DD') order by day asc", ['day','value'], cn)
     holdingsDF = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='{indicator}' and day >= to_date('{date_from}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)

     chart_range = get_range(priceDF, holdingsDF) if limited_range else None   
     holdingsDF  = get_values_in_usd(priceDF, holdingsDF) if chart_currency.upper() == PROPERTY_USD_CODE else holdingsDF
     cn.close_connection()           

     graph = btcchart.get_nupl_chart(priceDF, 
                                     holdingsDF, 
                                     PROPERTY_PRICE_CHART_VALUE_COLUMN, 
                                     PROPERTY_VALUE_CHART_VALUE_COLUMN, 
                                     PROPERTY_PRICE_SIGN,
                                     metric_unit,
                                     PROPERTY_PRICE_CHART_TITLE, 
                                     label, 
                                     PROPERTY_PRICE_CHART_LABEL, 
                                     metric_label, 
                                     filled,
                                     chart_currency,
                                     chart_range,
                                     height,
                                     width,
                                     show_full,
                                     secondary_chart_type)
       
          
     return graph

def get_mvrv_chart(date_from = '2010-08-01', width = None, height = 800, show_full = True):

     cn = PostgresConn() 
     priceDF = get_df_from_query(f"select day, calculated_value as value from general_indicator where indicator_name = 'bitcoin_price' and day >= to_date('{date_from}', 'YYYY-MM-DD') order by day asc", ['day','value'], cn)
     holdingsDF = get_df_from_query(f"select day, calculated_value from general_indicator where indicator_name='mvrv_value' and day >= to_date('{date_from}', 'YYYY-MM-DD')  order by day asc", ['day','calculated_value'], cn)

     cn.close_connection()           

     graph = btcchart.get_mvrv_chart(priceDF, 
                                     holdingsDF, 
                                     PROPERTY_PRICE_CHART_VALUE_COLUMN, 
                                     PROPERTY_VALUE_CHART_VALUE_COLUMN, 
                                     PROPERTY_PRICE_SIGN,
                                     "",
                                     PROPERTY_PRICE_CHART_TITLE, 
                                     "MVRV Z-Score", 
                                     PROPERTY_PRICE_CHART_LABEL, 
                                     "Score", 
                                     width,
                                     height,
                                     show_full)
       
          
     return graph


def get_sopr_chart(indicator, label, metric_label, metric_unit, date_from = PROPERTY_CHARTS_DEFAULT_VALID_FROM, height = PROPERTY_CHART_DEFAULT_HEIGHT, show_full = True):


     cn = PostgresConn() 
     priceDF = get_df_from_query(f"select day, calculated_value as value \
                                     from general_indicator \
                                    where indicator_name = 'bitcoin_price' \
                                      and day >= to_date('{date_from}', 'YYYY-MM-DD') \
                                    order by day asc", 
                                  ['day','value'], 
                                  cn)

     holdingsDF = get_df_from_query(f"select day, calculated_value \
                                        from general_indicator \
                                       where indicator_name='{indicator}' \
                                         and day >= to_date('{date_from}', 'YYYY-MM-DD') \
                                       order by day asc", 
                                     ['day','calculated_value'], 
                                     cn)
     cn.close_connection()          

     graph = btcchart.get_sopr_chart(priceDF, 
                                        holdingsDF, 
                                        PROPERTY_PRICE_CHART_VALUE_COLUMN, 
                                        PROPERTY_VALUE_CHART_VALUE_COLUMN, 
                                        PROPERTY_PRICE_SIGN,
                                        metric_unit,
                                        PROPERTY_PRICE_CHART_TITLE, 
                                        label, 
                                        PROPERTY_PRICE_CHART_LABEL, 
                                        metric_label, 
                                        height,
                                        show_full)
    
          
     return graph


def get_profit_vs_loss_chart():

     cn = PostgresConn()  

     priceDF = get_df_from_query(f"select day, calculated_value as value \
                                     from general_indicator \
                                    where indicator_name = 'bitcoin_price' \
                                      and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD') \
                                    order by day asc", 
                                   ['day','value'], 
                                   cn)

     profitDF = get_df_from_query(f"select day, calculated_value from general_indicator \
                                     where indicator_name='perc_of_addr_in_profit' \
                                       and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD') \
                                     order by day asc", 
                                   ['day','calculated_value'], 
                                   cn)

     lossDF = get_df_from_query(f"select day, calculated_value \
                                    from general_indicator \
                                   where indicator_name='perc_of_addr_in_loss' \
                                     and day >= to_date('{PROPERTY_CHARTS_DEFAULT_VALID_FROM}', 'YYYY-MM-DD') \
                                   order by day asc", 
                                 ['day','calculated_value'], 
                                 cn)
     cn.close_connection()   

     listDF = {
               "profit": {
                    "df": profitDF,
                    "name": "Addresses in profit",
                    "color": "#85bcbe",
                    "label": "% of addresses in profit",
                    "description": "Value",
                    "unit": "%"
               },
               "loss": {
                    "df": lossDF,
                    "name":  "Addresses in loss",
                    "color": "#a94c68",
                    "label": "% of addresses in loss",
                    "description": "Value",
                    "unit": "%"
               }
     }



     graph = btcchart.get_special_comparison_chart(priceDF, 
                                                   listDF,
                                                   PROPERTY_PRICE_CHART_VALUE_COLUMN, 
                                                   PROPERTY_VALUE_CHART_VALUE_COLUMN, 
                                                   PROPERTY_PRICE_SIGN,
                                                   PROPERTY_PRICE_CHART_TITLE, 
                                                   PROPERTY_PRICE_CHART_LABEL, 
                                                   'Profit Distribution (% addresses in profit vs loss)',
                                                   None)

     return graph



def get_addresses_perc_details(days_back):


     sql_query = f"select indicator_name, day, calculated_value \
                     from general_indicator \
                    where indicator_name in ('plankton_percentage',\
                                             'shrimps_percentage',\
                                             'crabs_percentage',\
                                             'fish_percentage',\
                                             'sharks_percentage',\
                                             'whales_percentage',\
                                             'humpbacks_percentage'\
                                             )"
                     
     columns = ['indicator_name', 'day','calculated_value']
     addDetailsList = {
                         "plankton": {
                                        "title": "Plankton",
                                        "desc": "(less then 0.01 BTC)"
                                     },
                          "shrimps": {
                                        "title": "Shrimps",
                                        "desc": "(between 0.01 and 1 BTC)",
                                     },
                            "crabs": {
                                        "title": "Crabs",  
                                        "desc": "(between 1 and 10 BTC)"            
                                     },
                             "fish": {
                                        "title": "Fish",
                                        "desc": "(between 10 and 100 BTC)"         
                                     },
                           "sharks": {
                                        "title": "Sharks", 
                                        "desc": "(between 100 and 1,000 BTC)"                                          
                                     },
                           "whales": {  
                                        "title": "Whales",
                                        "desc": "(between 1,000 and 10,000 BTC)"                                              
                                     },
                        "humpbacks": {
                                        "title": "Humpbacks",
                                        "desc": "(more then 10,000 BTC)"                                               
                                     } 
                    }


     return get_indicators_perc_details(days_back, sql_query, columns, addDetailsList, "", "_percentage")



def get_etf_bal_details(days_back):


     sql_query = "select indicator_name, day, calculated_value \
                    from general_indicator \
                   where indicator_name in ('wallettracker_totaletf_total_balance', \
                                            'wallettracker_blackrock',\
                                            'wallettracker_fidelity',\
                                            'wallettracker_bitwise',\
                                            'wallettracker_ark',\
                                            'wallettracker_wisdomtree',\
                                            'wallettracker_vaneck'\
                                           )"

     columns = ['indicator_name', 'day','calculated_value']

     addDetailsList = {
                         "totaletf_total_balance": {
                                                       "title": "All Spot ETFs",
                                                       "desc": ""
                                                  },
                                   "blackrock": {
                                                       "title": "iShares Bitcoin Trust (IBIT)",
                                                       "desc": "",
                                                  },
                                        "fidelity": {
                                                       "title": "Fidelity Wise Origin Bitcoin Fund (FBTC)",  
                                                       "desc": ""            
                                                  },
                                        "bitwise": {
                                                       "title": "Bitwise Bitcoin Fund (BITB)",
                                                       "desc": ""         
                                                  },
                                             "ark": {
                                                       "title": "21Shares Bitcoin ETP (ARKB)", 
                                                       "desc": ""                                          
                                                  },
                                   "wisdomtree": {  
                                                       "title": "WisdomTree Bitcoin Fund (BTCW)",
                                                       "desc": ""                                              
                                                  },
                                        "vaneck": {
                                                       "title": "VanEck Bitcoin Trust (HODL)",
                                                       "desc": ""                                               
                                                  } 
                    }

     return get_indicators_perc_details(days_back, sql_query, columns, addDetailsList, "wallettracker_", "")


def get_exchanges_bal_details(days_back):

     sql_query = "select indicator_name, day, calculated_value \
                    from general_indicator \
                   where indicator_name in ('wallettracker_coinbase', \
                                            'wallettracker_gemini', \
                                            'wallettracker_mtgox', \
                                            'wallettracker_binance', \
                                            'wallettracker_kraken', \
                                            'wallettracker_bitstamp'\
                                           )"

     columns = ['indicator_name', 'day','calculated_value']

     addDetailsList = {
                         "binance": {
                                        "title": "Binance Exchange",
                                        "desc": "",
                                     },
                         "bitstamp": {
                                        "title": "Bitsamp Exchange",
                                        "desc": "",
                                     },
                         "coinbase": {
                                        "title": "Coinbase Exchange",
                                        "desc": "",
                                     },
                           "gemini": {
                                        "title": "Gemini Exchange",  
                                        "desc": ""            
                                     },
                           "kraken": {
                                        "title": "Kraken Exchange",
                                        "desc": "",
                                     },
                            "mtgox": {
                                        "title": "Mt Gox Exchange",  
                                        "desc": ""            
                                     }
                    }

     
     return get_indicators_perc_details(days_back, sql_query, columns, addDetailsList, "wallettracker_", "")


