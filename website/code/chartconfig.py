import json

class Chartconfig:
    config = {
                "addresses": {
                                        "activity": {
                                                        "total":   {
                                                                        "label": "Number of active addresses holding all BTC",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "normal",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "total_activity",
                                                                                        "7dma":   "total_activity_7dma",
                                                                                        "21dma":  "total_activity_21dma"
                                                                                    }
                                                                    },
                                                        "plankton": {
                                                                        "label": "Number of active addresses holding less then 0.01 BTC (Plankton)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "plankton_activity",
                                                                                        "7dma":   "plankton_activity_7dma",
                                                                                        "21dma":  "plankton_activity_21dma"
                                                                                    }
                                                                    },
                                                        "shrimps": {
                                                                        "label": "Number of active addresses holding between 0.1 and 1 BTC (Shrimps)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "shrimps_activity",
                                                                                        "7dma":   "shrimps_activity_7dma",
                                                                                        "21dma":  "shrimps_activity_21dma"
                                                                                    }
                                                                    },
                                                        "crabs":    {
                                                                        "label": "Number of active addresses between 1 and 10 BTC (Crabs)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "crabs_activity",
                                                                                        "7dma":   "crabs_activity_7dma",
                                                                                        "21dma":  "crabs_activity_21dma"
                                                                                    } 
                                                                    },
                                                        "fish":     {
                                                                        "label": "Number of active addresses holding between 10 and 100 BTC (Fish)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "fish_activity",
                                                                                        "7dma":   "fish_activity_7dma",
                                                                                        "21dma":  "fish_activity_21dma"
                                                                                    }
                                                                    },
                                                        "sharks":   {
                                                                        "label": "Number of active addresses holding between 100 and 1,000 BTC (Sharks)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "sharks_activity",
                                                                                        "7dma":   "sharks_activity_7dma",
                                                                                        "21dma":  "sharks_activity_21dma"
                                                                                    } 
                                                                    },
                                                        "whales":   {
                                                                        "label": "Number of active addressesholding between 1,000 and 10,000 BTC (Whales)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "whales_activity",
                                                                                        "7dma":   "whales_activity_7dma",
                                                                                        "21dma":  "whales_activity_21dma"
                                                                                    } 
                                                                    },  
                                                        "humpbacks":{
                                                                        "label": "Number of active addresses holding more then 10,000 BTC (Humpbacks)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "humpbacks_activity",
                                                                                        "7dma":   "humpbacks_activity_7dma",
                                                                                        "21dma":  "humpbacks_activity_21dma"
                                                                                    } 
                                                                    }           
                                                    },
                                       "balances":  {
                                                        "total":    {
                                                                        "label": "Balance on addresses holding all BTC",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "normal",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "total_balance",
                                                                                        "7dma":   "total_balance_7dma",
                                                                                        "21dma":  "total_balance_21dma"
                                                                                    }
                                                                    },
                                                        "plankton": {
                                                                        "label": "Balance on addresses holding less then 0.01 BTC (Plankton)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "plankton_balance",
                                                                                        "7dma":   "plankton_balance_7dma",
                                                                                        "21dma":  "plankton_balance_21dma"
                                                                                    }
                                                                    },
                                                        "shrimps":  {
                                                                        "label": "Balance on addresses holding between 0.1 and 1 BTC (Shrimps)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "shrimps_balance",
                                                                                        "7dma":   "shrimps_balance_7dma",
                                                                                        "21dma":  "shrimps_balance_21dma"
                                                                                    }
                                                                    },
                                                        "crabs":    {
                                                                        "label": "Balance on addresses holding between 1 and 10 BTC (Crabs)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "crabs_balance",
                                                                                        "7dma":   "crabs_balance_7dma",
                                                                                        "21dma":  "crabs_balance_21dma"
                                                                                    } 
                                                                    },
                                                        "fish":     {
                                                                        "label": "Balance on addresses holding between 10 and 100 BTC (Fish)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "fish_balance",
                                                                                        "7dma":   "fish_balance_7dma",
                                                                                        "21dma":  "fish_balance_21dma"
                                                                                    }
                                                                    },
                                                        "sharks": {
                                                                        "label": "Balance on addresses holding between 100 and 1,000 BTC (Sharks)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "sharks_balance",
                                                                                        "7dma":   "sharks_balance_7dma",
                                                                                        "21dma":  "sharks_balance_21dma"
                                                                                    } 
                                                                    },
                                                        "whales":   {
                                                                        "label": "Balance on addresses holding between 1,000 and 10,000 BTC (Whales)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "whales_balance",
                                                                                        "7dma":   "whales_balance_7dma",
                                                                                        "21dma":  "whales_balance_21dma"
                                                                                    } 
                                                                    },  
                                                        "humpbacks":{
                                                                        "label": "Balance on addresses holding more then 10,000 BTC (Humpbacks)",
                                                                        "value_label": "Balance",
                                                                        "value_unit": "BTC",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "btc",
                                                                        "precision_selector": True,
                                                                        "currency_selector": True,
                                                                        "fillunder": True,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "humpbacks_balance",
                                                                                        "7dma":   "humpbacks_balance_7dma",
                                                                                        "21dma":  "humpbacks_balance_21dma"
                                                                                    } 
                                                                    }           
                                                    },
                                        "counts":   {
                                                        "total":    {
                                                                        "label": "Number of addresses holding all BTC",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "normal",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "total_count",
                                                                                        "7dma":   "total_count_7dma",
                                                                                        "21dma":  "total_count_21dma"
                                                                                    } 
                                                                    },
                                                        "plankton": {
                                                                        "label": "Number of addresses holding less then 0.01 BTC (Plankton)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "plankton_count",
                                                                                        "7dma":   "plankton_count_7dma",
                                                                                        "21dma":  "plankton_count_21dma"
                                                                                    } 
                                                                    },
                                                        "shrimps":  {
                                                                        "label": "Number of addresses holding between 0.1 and 1 BTC (Shrimps)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "shrimps_count",
                                                                                        "7dma":   "shrimps_count_7dma",
                                                                                        "21dma":  "shrimps_count_21dma"
                                                                                    } 
                                                                    },
                                                        "crabs":    {
                                                                        "label": "Number of addresses holding between 1 and 10 BTC (Crabs)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "crabs_count",
                                                                                        "7dma":   "crabs_count_7dma",
                                                                                        "21dma":  "crabs_count_21dma"
                                                                                    }  
                                                                    },
                                                        "fish":     {
                                                                        "label": "Number of addresses holding between 10 and 100 BTC (Fish)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "fish_count",
                                                                                        "7dma":   "fish_count_7dma",
                                                                                        "21dma":  "fish_count_21dma"
                                                                                    } 
                                                                    },
                                                        "sharks":   {
                                                                        "label": "Number of addresses holding between 100 and 1,000 BTC (Sharks)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "sharks_count",
                                                                                        "7dma":   "sharks_count_7dma",
                                                                                        "21dma":  "sharks_count_21dma"
                                                                                    } 
                                                                    },
                                                        "whales":   {
                                                                        "label": "Number of addressesholding between 1,000 and 10,000 BTC (Whales)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "whales_count",
                                                                                        "7dma":   "whales_count_7dma",
                                                                                        "21dma":  "whales_count_21dma"
                                                                                    }  
                                                                    },  
                                                        "humpbacks":{
                                                                        "label": "Number of addresses holding more then 10,000 BTC (Humpbacks)",
                                                                        "value_label": "Number of addresses",
                                                                        "value_unit": "",
                                                                        "default_precision": "7dma",
                                                                        "default_currency": "",
                                                                        "precision_selector": True,
                                                                        "currency_selector": False,
                                                                        "fillunder": False,
                                                                        "chart_date_from": "2010-07-01",
                                                                        "widget_active": True,
                                                                        "indicators": {
                                                                                        "normal": "humpbacks_count",
                                                                                        "7dma":   "humpbacks_count_7dma",
                                                                                        "21dma":  "humpbacks_count_21dma"
                                                                                    }  
                                                                    }           
                                                    },
                                    "distribution": {
                                                        "label": "Distribution Across Address Types",
                                                        "default_precision": "normal",
                                                        "precision_selector": False,
                                                        "currency_selector": False,
                                                        "default_currency": "",
                                                        "chart_date_from": "2010-07-01",
                                                        "widget_active": True,
                                                        "indicators": {}
                                                        
                                                    }
                            },
            "mining":{
                            "rewards": {
                                                            "total_rewards":{
                                                                                "label": "Miners' Revenue from Block Rewards",
                                                                                "value_label": "Rewards",
                                                                                "value_unit": "BTC",
                                                                                "default_precision": "7dma",
                                                                                "default_currency": "btc",
                                                                                "precision_selector": True,
                                                                                "currency_selector": True,
                                                                                "fillunder": True,
                                                                                "chart_date_from": "2010-09-01",
                                                                                "widget_active": True,
                                                                                "indicators": {
                                                                                                "normal": "miners_revenue_total_rewards",
                                                                                                "7dma":   "miners_revenue_total_rewards_7dma",
                                                                                                "21dma":  "miners_revenue_total_rewards_21dma"
                                                                                            }  
                                                                            },
                                                            "total_fees":{
                                                                                "label": "Miners' Revenue from Fees",
                                                                                "value_label": "Fees",
                                                                                "value_unit": "BTC",
                                                                                "default_precision": "7dma",
                                                                                "default_currency": "btc",
                                                                                "precision_selector": True,
                                                                                "currency_selector": True,
                                                                                "fillunder": True,
                                                                                "chart_date_from": "2010-09-01",
                                                                                "widget_active": True,
                                                                                "indicators": {
                                                                                                "normal": "miners_revenue_total_fees",
                                                                                                "7dma":   "miners_revenue_total_fees_7dma",
                                                                                                "21dma":  "miners_revenue_total_fees_21dma"
                                                                                            }  
                                                                            },
                                                            "total_revenue":{
                                                                            "label": "Total Miners' Revenue: Fees and Block Rewards",
                                                                            "value_label": "Fees",
                                                                            "value_unit": "BTC",
                                                                            "default_precision": "7dma",
                                                                            "default_currency": "btc",
                                                                            "precision_selector": True,
                                                                            "currency_selector": True,
                                                                            "fillunder": True,
                                                                            "chart_date_from": "2010-09-01",
                                                                            "widget_active": True,
                                                                            "indicators": {
                                                                                            "normal": "miners_revenue_total_revenue",
                                                                                            "7dma":   "miners_revenue_total_revenue_7dma",
                                                                                            "21dma":  "miners_revenue_total_revenue_21dma"
                                                                                        }  
                                                                        },
                                                "block_rewards_vs_fees":{
                                                                            "label": "Miners Revenue (Block Rewards vs Fees)",
                                                                            "value_label": "Block Rewards vs Fees",
                                                                            "value_unit": "BTC",
                                                                            "default_precision": "7dma",
                                                                            "default_currency": "btc",
                                                                            "precision_selector": False,
                                                                            "currency_selector": False,
                                                                            "fillunder": True,
                                                                            "chart_date_from": "2010-09-01",
                                                                            "widget_active": False,
                                                                            "indicators": {
                                                                                            "normal": "miners_revenue_block_rewards_vs_fees",
                                                                                            "7dma":   "miners_revenue_block_rewards_vs_fees_7dma",
                                                                                            "21dma":  "miners_revenue_block_rewards_vs_fees_21dma"
                                                                                        }  
                                                                        },
                                                "fee_ratioo_multiple":{
                                                                            "label": "The Fee Ratio Multiple (FRM)",
                                                                            "value_label": "Ratio",
                                                                            "value_unit": "",
                                                                            "default_precision": "21dma",
                                                                            "default_currency": "btc",
                                                                            "precision_selector": True,
                                                                            "currency_selector": False,
                                                                            "fillunder": True,
                                                                            "chart_date_from": "2010-09-01",
                                                                            "widget_active": False,
                                                                            "indicators": {
                                                                                            "normal": "miners_revenue_fee_ratioo_multiple",
                                                                                            "7dma":   "miners_revenue_fee_ratioo_multiple_7dma",
                                                                                            "21dma":  "miners_revenue_fee_ratioo_multiple_21dma"
                                                                                        }  
                                                                        }
                                    },
                         "volumes": {
                                            "num_of_transactions":{
                                                                    "label": "Average Number of Bitcoin Transactions Per Day",
                                                                    "value_label": "Avg num of transactions",
                                                                    "value_unit": "",
                                                                    "default_precision": "7dma",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": False,
                                                                    "fillunder": True,
                                                                    "chart_date_from": "2010-09-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "miners_revenue_num_of_transactions",
                                                                                    "7dma":   "miners_revenue_num_of_transactions_7dma",
                                                                                    "21dma":  "miners_revenue_num_of_transactions_21dma"
                                                                                }  
                                                                },
                                                "num_of_blocks":{
                                                                    "label": "Average Number of Bitcoin Blocks Mined Per Day",
                                                                    "value_label": "Avg num of blocks",
                                                                    "value_unit": "",
                                                                    "default_precision": "7dma",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": False,
                                                                    "fillunder": True,
                                                                    "chart_date_from": "2010-09-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "miners_revenue_num_of_blocks",
                                                                                    "7dma":   "miners_revenue_num_of_blocks_7dma",
                                                                                    "21dma":  "miners_revenue_num_of_blocks_21dma"
                                                                                }  
                                                                },
                                            "avg_fee_per_transaction":{
                                                                    "label": "Average Fees Paid Per Bitcoin Transaction",
                                                                    "value_label": "Avarege fee",
                                                                    "value_unit": "BTC",
                                                                    "default_precision": "7dma",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": True,
                                                                    "fillunder": True,
                                                                    "chart_date_from": "2010-09-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "miners_revenue_avg_fee_per_transaction",
                                                                                    "7dma":   "miners_revenue_avg_fee_per_transaction_7dma",
                                                                                    "21dma":  "miners_revenue_avg_fee_per_transaction_21dma"
                                                                                }  
                                                                },
                                            "avg_fee_per_block":{
                                                                    "label": "Average Fees Paid Per Bitcoin Block",
                                                                    "value_label": "Avg fee for block",
                                                                    "value_unit": "BTC",
                                                                    "default_precision": "7dma",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": True,
                                                                    "fillunder": True,
                                                                    "chart_date_from": "2010-09-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "miners_revenue_avg_fee_per_block",
                                                                                    "7dma":   "miners_revenue_avg_fee_per_block_7dma",
                                                                                    "21dma":  "miners_revenue_avg_fee_per_block_21dma"
                                                                                }  
                                                                }
                                    },
                   "transfervolume":{
                                        "transfervolume":{
                                                            "label": "Daily Transfer Volume of Bitcoin",
                                                            "value_label": "Transfer Volume",
                                                            "value_unit": "BTC",
                                                            "default_precision": "7dma",
                                                            "default_currency": "btc",
                                                            "precision_selector": True,
                                                            "currency_selector": True,
                                                            "fillunder": True,
                                                            "chart_date_from": "2010-07-01",
                                                            "widget_active": True,
                                                            "indicators": {
                                                                            "normal": "transfervolume_volume",
                                                                            "7dma":   "transfervolume_volume_7dma",
                                                                            "21dma":  "transfervolume_volume_21dma"
                                                                         }  
                                                        }
                                    }
                    },
                   "supply":{
                                                     "issuance":{
                                                                    "label": "Bitcoin Issuance",
                                                                    "value_label": "Issuance",
                                                                    "value_unit": "BTC",
                                                                    "default_precision": "7dma",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": True,
                                                                    "fillunder": True,
                                                                    "chart_date_from": "2010-01-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "supply_issuance",
                                                                                    "7dma":   "supply_issuance_7dma",
                                                                                    "21dma":  "supply_issuance_21dma"
                                                                                }  
                                                                },
                                           "circulating_supply":{
                                                                    "label": "Bitcoin Circulating Supply",
                                                                    "value_label": "Supply",
                                                                    "value_unit": "BTC",
                                                                    "default_precision": "normal",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": True,
                                                                    "fillunder": False,
                                                                    "chart_date_from": "2010-01-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "supply_circulating_supply",
                                                                                    "7dma":   "supply_circulating_supply_7dma",
                                                                                    "21dma":  "supply_circulating_supply_21dma"
                                                                                }  
                                                                },
                                              "daily_inflation":{
                                                                "label": "Bitcoin's Daily Inflation Rate",
                                                                "value_label": "Daily Inflation Rate",
                                                                "value_unit": "%",
                                                                "default_precision": "normal",
                                                                "default_currency": "%",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-09-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "supply_daily_inflation",
                                                                                "7dma":   "supply_daily_inflation_7dma",
                                                                                "21dma":  "supply_daily_inflation_21dma"
                                                                            }  
                                                            },
                                         "annual_inflation":{
                                                                "label": "Bitcoin's Annual Inflation Rate",
                                                                "value_label": "Annual Inflation Rate",
                                                                "value_unit": "%",
                                                                "default_precision": "normal",
                                                                "default_currency": "%",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-09-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "supply_annual_inflation",
                                                                                "7dma":   "supply_annual_inflation_7dma",
                                                                                "21dma":  "supply_annual_inflation_21dma"
                                                                            }  
                                                            }
                            },
                "institutions":{
                                "exchanges":{
                                                        "mtgox":{
                                                                    "label": "Mt. Gox Trustee",
                                                                    "value_label": "Balance",
                                                                    "value_unit": "BTC",
                                                                    "default_precision": "normal",
                                                                    "default_currency": "btc",
                                                                    "precision_selector": True,
                                                                    "currency_selector": True,
                                                                    "fillunder": True,
                                                                    "chart_date_from": "2010-07-01",
                                                                    "widget_active": True,
                                                                    "indicators": {
                                                                                    "normal": "wallettracker_mtgox",
                                                                                    "7dma":   "wallettracker_mtgox_7dma",
                                                                                    "21dma":  "wallettracker_mtgox_21dma"
                                                                                }  
                                                                },
                                                     "coinbase":{
                                                                "label": "Balance of BTC on Coinbase Exchange",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_coinbase",
                                                                                "7dma":   "wallettracker_coinbase_7dma",
                                                                                "21dma":  "wallettracker_coinbase_21dma"
                                                                            }  
                                                            },
                                                   "gemini":{
                                                                "label": "Balance of BTC on Gemini Exchange",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_gemini",
                                                                                "7dma":   "wallettracker_gemini_7dma",
                                                                                "21dma":  "wallettracker_gemini_21dma"
                                                                            }  
                                                            },
                                                   "kraken":{
                                                                "label": "Balance of BTC on Kraken Exchange",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_kraken",
                                                                                "7dma":   "wallettracker_kraken_7dma",
                                                                                "21dma":  "wallettracker_kraken_21dma"
                                                                            }  
                                                            },
                                                  "binance":{
                                                                "label": "Balance of BTC on Binance Exchange",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_binance",
                                                                                "7dma":   "wallettracker_binance_7dma",
                                                                                "21dma":  "wallettracker_binance_21dma"
                                                                            }  
                                                            },
                                                 "bitstamp":{
                                                                "label": "Balance of BTC on Bistamp Exchange",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": False,
                                                                "indicators": {
                                                                                "normal": "wallettracker_bitstamp",
                                                                                "7dma":   "wallettracker_bitstamp_7dma",
                                                                                "21dma":  "wallettracker_bitstamp_21dma"
                                                                            }  
                                                            }
                                    },
                        "etfs":{
                                                    "blackrock":{
                                                                "label": "Balance of BTC on iShares Bitcoin Trust (IBIT) Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_blackrock",
                                                                                "7dma":   "wallettracker_blackrock_7dma",
                                                                                "21dma":  "wallettracker_blackrock_21dma"
                                                                            }  
                                                            },
                                                  "fidelity":{
                                                                "label": "Balance of BTC on Fidelity Wise Origin Bitcoin Fund (FBTC) Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_fidelitycustody",
                                                                                "7dma":   "wallettracker_fidelitycustody_7dma",
                                                                                "21dma":  "wallettracker_fidelitycustody_21dma"
                                                                            }  
                                                            },
                                                  "bitwise":{
                                                                "label": "Balance of BTC on Bitwise Bitcoin Fund (BITB) Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_bitwise",
                                                                                "7dma":   "wallettracker_bitwise_7dma",
                                                                                "21dma":  "wallettracker_bitwise_21dma"
                                                                            }  
                                                            },
                                                  "ark":{
                                                                "label": "Balance of BTC on 21Shares Bitcoin ETP (ARKB) Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_arkinvest",
                                                                                "7dma":   "wallettracker_arkinvest_7dma",
                                                                                "21dma":  "wallettracker_arkinvest_21dma"
                                                                            }  
                                                            },
                                                "wisdomtree":{
                                                                "label": "Balance of BTC on WisdomTree Bitcoin Fund (BTCW) Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_wisdomtree",
                                                                                "7dma":   "wallettracker_wisdomtree_7dma",
                                                                                "21dma":  "wallettracker_wisdomtree_21dma"
                                                                            }  
                                                            },
                                                   "vaneck":{
                                                                "label": "Balance of BTC on VanEck Bitcoin Trust (HODL) Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_vaneck",
                                                                                "7dma":   "wallettracker_vaneck_7dma",
                                                                                "21dma":  "wallettracker_vaneck_21dma"
                                                                            }  
                                                            },
                                                 "totaletf":{
                                                                "label": "Bitcoin Holdings in Spot ETFs",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "21dma",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_totaletf_total_balance",
                                                                                "7dma":   "wallettracker_totaletf_total_balance_7dma",
                                                                                "21dma":  "wallettracker_totaletf_total_balance_21dma"
                                                                            }  
                                                            }
                    },
                    "other":{
                                                "tesla":{
                                                                "label": "Balance of BTC on Tesla Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "normal",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_tesla",
                                                                                "7dma":   "wallettracker_tesla_7dma",
                                                                                "21dma":  "wallettracker_tesla_21dma"
                                                                              }  
                                                                },                                                                                                            
                                                  "satoshi":{
                                                                "label": "Balance of BTC on Satoshi Nakamoto's Addresses",
                                                                "value_label": "Balance",
                                                                "value_unit": "BTC",
                                                                "default_precision": "normal",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "wallettracker_satoshinakamoto",
                                                                                "7dma":   "wallettracker_satoshinakamoto_7dma",
                                                                                "21dma":  "wallettracker_satoshinakamoto_21dma"
                                                                            }  
                                                            }
                    }
                },
               "onchain":{

                    "sopr":{
                                                    "sopr":{
                                                                "label": "Spent Output Profit Ratio (SOPR)",
                                                                "value_label": "SOPR",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_date_from": "2012-01-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "sopr_value",
                                                                                "7dma":   "sopr_value_7dma",
                                                                                "21dma":  "sopr_value_21dma"
                                                                            }  
                                                            },
                                                 "sth_sopr":{
                                                                "label": "Spent Output Profit Ratio (SOPR) - Short Term Hodler",
                                                                "value_label": "SOPR",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_date_from": "2012-01-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "sth_sopr_value",
                                                                                "7dma":   "sth_sopr_value_7dma",
                                                                                "21dma":  "sth_sopr_value_21dma"
                                                                            }  
                                                            },
                                                 "lth_sopr":{
                                                                "label": "Spent Output Profit Ratio (SOPR) - Long Term Hodler",
                                                                "value_label": "SOPR",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_date_from": "2012-01-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "lth_sopr_value",
                                                                                "7dma":   "lth_sopr_value_7dma",
                                                                                "21dma":  "lth_sopr_value_21dma"
                                                                            }  
                                                            },
                    },
                    "realizedprice": {
                                            "realizedprice":{
                                                                "label": "Realized Price",
                                                                "value_label": "RP",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_type": "log",
                                                                "chart_date_from": "2010-09-30",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "realized_price",
                                                                                "7dma":   "realized_price_7dma",
                                                                                "21dma":  "realized_price_21dma"
                                                                            }  
                                                            },
                                        "sth_realizedprice":{
                                                                "label": "Realized Price - Short Term Hodler",
                                                                "value_label": "RPSTH",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_type": "log",
                                                                "chart_date_from": "2010-09-30",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "realized_sth_price",
                                                                                "7dma":   "realized_sth_price_7dma",
                                                                                "21dma":  "realized_sth_price_21dma"
                                                                            }  
                                                            },
                                        "lth_realizedprice":{
                                                                "label": "Realized Price - Long Term Hodler",
                                                                "value_label": "RPLTH",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_type": "log",
                                                                "chart_date_from": "2010-09-30",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "realized_lth_price",
                                                                                "7dma":   "realized_lth_price_7dma",
                                                                                "21dma":  "realized_lth_price_21dma"
                                                                            }  
                                                            }
                    },
                    "supply": {
                                               "sth_supply":{
                                                                "label": "Supply - Short Term Hodler",
                                                                "value_label": "STH Supply",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-05-30",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "sth_balance",
                                                                                "7dma":   "sth_balance_7dma",
                                                                                "21dma":  "sth_balance_21dma"
                                                                            }  
                                                            },
                                               "lth_supply":{
                                                                "label": "Supply - Long Term Hodler",
                                                                "value_label": "LTH Supply",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "btc",
                                                                "precision_selector": True,
                                                                "currency_selector": True,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-05-30",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "lth_balance",
                                                                                "7dma":   "lth_balance_7dma",
                                                                                "21dma":  "lth_balance_21dma"
                                                                            }  
                                                            }
                    },
                    "profitloss": {
                                      "addresses_in_profit":{
                                                                "label": "Percentage of Addresses in Profit",
                                                                "value_label": "% of addresses in profit",
                                                                "value_unit": "%",
                                                                "default_precision": "7dma",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "perc_of_addr_in_profit",
                                                                                "7dma":   "perc_of_addr_in_profit_7dma",
                                                                                "21dma":  "perc_of_addr_in_profit_21dma"
                                                                            }  
                                                            },
                                        "addresses_in_loss":{
                                                                "label": "Percentage of Addresses in Loss",
                                                                "value_label": "% of addresses in loss",
                                                                "value_unit": "%",
                                                                "default_precision": "7dma",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "perc_of_addr_in_loss",
                                                                                "7dma":   "perc_of_addr_in_loss_7dma",
                                                                                "21dma":  "perc_of_addr_in_loss_21dma"
                                                                            }  
                                                            },
                             "addresses_in_profit_vs_loss": {
                                                                "label": "Percentage of Addresses in Profit vs Loss",
                                                                "value_label": "% of addresses in profit vs % of addresses in loss",
                                                                "value_unit": "%",
                                                                "default_precision": "normal",
                                                                "precision_selector": False,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "default_currency": "",
                                                                "chart_date_from": "2010-07-01",
                                                                "widget_active": False,
                                                                "indicators": {
                                                                                    "normal": "",
                                                                                    "7dma": "",
                                                                                    "21dma": ""
                                                                                }
                                                                
                                                            }
                    },
                    "other": {
                                                      "cdd":{
                                                                "label": "Coin Days Destroyed (CDD)",
                                                                "value_label": "CDD",
                                                                "value_unit": "",
                                                                "default_precision": "90dma",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "cdd",
                                                                                "7dma":   "cdd_7dma",
                                                                                "21dma":  "cdd_21dma",
                                                                                "30dma":  "cdd_30dma",
                                                                                "90dma":  "cdd_90dma"
                                                                            }  
                                                            },
                                                    "sacdd":{
                                                                "label": "Supply Adjusted Coin Days Destroyed",
                                                                "value_label": "SACDD",
                                                                "value_unit": "",
                                                                "default_precision": "90dma",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": True,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "adj_cdd",
                                                                                "7dma":   "adj_cdd_7dma",
                                                                                "21dma":  "adj_cdd_21dma",
                                                                                "30dma":  "adj_cdd_30dma",
                                                                                "90dma":  "adj_cdd_90dma"
                                                                            }  
                                                            },
                                                     "nupl":{
                                                                "label": "Net Unrealized Profit/Loss (NUPL)",
                                                                "value_label": "NUPL",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "nupl",
                                                                                "7dma":   "nupl_7dma",
                                                                                "21dma":  "nupl_21dma"
                                                                            }  
                                                            },
                                   "unrealized_profit_loss":{
                                                                "label": "Unrealized Profit/Loss",
                                                                "value_label": "UPL",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": True,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "unrealized_profit_loss",
                                                                                "7dma":   "unrealized_profit_loss_7dma",
                                                                                "21dma":  "unrealized_profit_loss_21dma"
                                                                            }  
                                                            },
                                                    "mvrvz":{
                                                                "label": "MVRV Z-Score",
                                                                "value_label": "MVRV Z-Score",
                                                                "value_unit": "",
                                                                "default_precision": "normal",
                                                                "default_currency": "",
                                                                "precision_selector": False,
                                                                "currency_selector": False,
                                                                "fillunder": False,
                                                                "chart_date_from": "2010-11-01",
                                                                "widget_active": True,
                                                                "indicators": {
                                                                                "normal": "mvrvz_value"
                                                                              }  
                                                            }
                            }
                

                
                }
    }

    
    def __init__(self, category, metric, submetric, precision, currency):
        self.category = category
        self.metric = metric
        self.submetric = submetric
        self.precision = precision
        self.currency = currency

       
        # f = open("./conf/config.json")
        # config_data = json.load(f)



    def get_category(self):
        return self.category

    def get_metric(self):
        return self.metric

    def get_submetric(self):
        return self.submetric
    
    def get_precision(self):
        return self.precision

    def get_currency(self):
        return self.currency

    def get_details_obj(self):

        det_obj = None

        if self.metric != None:
            obj = self.config[self.category][self.metric]
            

            if self.submetric != None:
                det_obj = obj[self.submetric]
            else:
                det_obj = obj
        else:
            det_obj = self.config[self.category]

        return det_obj


    def get_label(self):       
        det_obj = self.get_details_obj()
        return det_obj['label']

    def get_label_with_dma(self):       
        det_obj = self.get_details_obj()
        return det_obj['label'] + " - " + self.get_active_precision().upper()

    def get_default_precision(self):      
        det_obj = self.get_details_obj()
        return det_obj['default_precision']


    def get_default_currency(self):  
        det_obj = self.get_details_obj()
        return det_obj['default_currency']


    def get_value_label(self):  
        det_obj = self.get_details_obj()
        return det_obj['value_label']

    def get_value_chart_start_date(self):  
        det_obj = self.get_details_obj()
        return det_obj['chart_date_from']

    def get_value_unit(self):  
        det_obj = self.get_details_obj()

        if self.currency == None or self.currency.upper() != 'USD':
            ret_val = det_obj['value_unit'].upper()
        else:
            ret_val = 'USD'

        return ret_val

    def get_active_precision(self):
        det_obj = self.get_details_obj()

        ret_prec = self.get_default_precision()

        if self.precision != None:
            ret_prec = self.precision
        
        return ret_prec

    def get_active_currency(self):
        det_obj = self.get_details_obj()

        ret_currency = self.get_default_currency()

        if self.currency != None:
            ret_currency = self.currency
        
        return ret_currency

    def get_indicator(self, level_of_details):
        det_obj = self.get_details_obj()
        lod = self.get_default_precision()

        if level_of_details != None:
            lod = level_of_details

        final_indicator = det_obj['indicators'][lod]

        return final_indicator

    def get_chart_type(self):  
        det_obj = self.get_details_obj()

        try:
            chart_type = det_obj['chart_type']
        except:
            chart_type = None

        return chart_type

    def is_precision_selector_enabled(self):  
        det_obj = self.get_details_obj()
        return det_obj['precision_selector']

    def is_currency_selector_enabled(self):  
        det_obj = self.get_details_obj()
        return det_obj['currency_selector']
    
    def is_fillunder(self):  
        det_obj = self.get_details_obj()
        return det_obj['fillunder']


        