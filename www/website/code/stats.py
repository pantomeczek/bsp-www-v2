from . import charts

PIE_CHART_CONFIG = {
    "addresses_activity": {
        "name": "Bitcoin Address Activity by Size (%)",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "plankton_activity", "indicator_label": "Plankton"},
            {"indicator_name": "shrimps_activity", "indicator_label": "Shrimps"},
            {"indicator_name": "crabs_activity", "indicator_label": "Crabs"},
            {"indicator_name": "fish_activity", "indicator_label": "Fish"},
            {"indicator_name": "sharks_activity", "indicator_label": "Sharks"},
            {"indicator_name": "whales_activity", "indicator_label": "Whales"},
            {"indicator_name": "humpbacks_activity", "indicator_label": "Humpbacks"}
        ],

    },
    "addresses_counts": {
        "name": "Address Distribution by Size Group (%)",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "plankton_count", "indicator_label": "Plankton"},
            {"indicator_name": "shrimps_count", "indicator_label": "Shrimps"},
            {"indicator_name": "crabs_count", "indicator_label": "Crabs"},
            {"indicator_name": "fish_count", "indicator_label": "Fish"},
            {"indicator_name": "sharks_count", "indicator_label": "Sharks"},
            {"indicator_name": "whales_count", "indicator_label": "Whales"},
            {"indicator_name": "humpbacks_count", "indicator_label": "Humpbacks"}
        ],

    },
    "addresses_balances": {
        "name": "Bitcoin Holdings by Address Size (%)",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "plankton_balance", "indicator_label": "Plankton"},
            {"indicator_name": "shrimps_balance", "indicator_label": "Shrimps"},
            {"indicator_name": "crabs_balance", "indicator_label": "Crabs"},
            {"indicator_name": "fish_balance", "indicator_label": "Fish"},
            {"indicator_name": "sharks_balance", "indicator_label": "Sharks"},
            {"indicator_name": "whales_balance", "indicator_label": "Whales"},
            {"indicator_name": "humpbacks_balance", "indicator_label": "Humpbacks"}
        ],

    },
    "mining_rewards": {
        "name": "Miner's Revenue - Blocks vs Fees",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "miners_revenue_total_rewards", "indicator_label": "Block Rewards"},
            {"indicator_name": "miners_revenue_total_fees", "indicator_label": "Fees"}
        ],

    },
    "onchain_supply": {
        "name": "Bitcoin Supply - STH vs LTH",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "sth_balance", "indicator_label": "Short-Term Hodler Bitcoin Supply"},
            {"indicator_name": "lth_balance", "indicator_label": "Long-Term Hodler Bitcoin Supply"}
        ],

    },
    "onchain_profitloss": {
        "name": "Percentage of Addresses - Profit vs Loss",
        "valus_type": "percent",
        "indicators": [
            {"indicator_name": "perc_of_addr_in_profit", "indicator_label": "Percentage of Addresses in Profit"},
            {"indicator_name": "perc_of_addr_in_loss", "indicator_label": "Percentage of Addresses in Loss"}
        ],

    },
    "institutions_etfs": {
        "name": "BTC Holdings on ETF Addresses",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "wallettracker_blackrock", "indicator_label": "iShares Bitcoin Trust (IBIT)"},
            {"indicator_name": "wallettracker_fidelitycustody", "indicator_label": "Fidelity Wise Origin Bitcoin Fund (FBTC)"},
            {"indicator_name": "wallettracker_bitwise", "indicator_label": "Bitwise Bitcoin Fund (BITB) "},
            {"indicator_name": "wallettracker_arkinvest", "indicator_label": "21Shares Bitcoin ETP (ARKB)"},
            {"indicator_name": "wallettracker_wisdomtree", "indicator_label": "WisdomTree Bitcoin Fund (BTCW)"},
            {"indicator_name": "wallettracker_vaneck", "indicator_label": "VanEck Bitcoin Trust (HODL)"}
        ]

    },
    "institutions_exchanges": {
        "name": "BTC Holdings on Exchanges",
        "valus_type": "value",
        "indicators": [
            {"indicator_name": "wallettracker_mtgox", "indicator_label": "Mt. Gox Trustee"},
            {"indicator_name": "wallettracker_coinbase", "indicator_label": "Coinbase Exchange"},
            {"indicator_name": "wallettracker_gemini", "indicator_label": "Gemini Exchange"},
            {"indicator_name": "wallettracker_kraken", "indicator_label": "Kraken Exchange"},
            {"indicator_name": "wallettracker_binance", "indicator_label": "Binance Exchange"}
        ]

    }
}

def get_pie_chart_data_from_df(crt, data_type):
    headers = []
    data = []

    label = 'day_0_raw' if data_type == 'value' else 'day_0_perc'
    for i in crt:
        headers.append(i['indicator_name'])
        data.append(round(i[label],2))

    return {"headers":headers, "data":data}



def get_stats_element(chart_type, metric):

    label = f"{chart_type}_{metric}"

    if label in PIE_CHART_CONFIG:
        el = PIE_CHART_CONFIG.get(label)
        crt = charts.get_activity_stats(el.get('indicators'))
        if crt is None:
            return []
        dt = get_pie_chart_data_from_df(crt, el.get('valus_type'))
        return [
                    {
                        "type":"stats",
                        "name": el.get('name'),
                        "statobj": crt
                    },
                    {
                        "id": f"chart_pie_{label}",
                        "type": "piechart",
                        "title": el.get('name'),
                        "href": '',
                        "chart": charts.get_pie_chart(height=427, data=dt, data_type=el.get('valus_type')),
                        "stats": None,
                    }

                ]
    else:
        return []