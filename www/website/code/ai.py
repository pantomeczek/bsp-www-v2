from .postgresql_connection import PostgresConn


QUERY = """
select analysis_date, analysis_content
  from ai_analysis
 where analysis_type = '##ANALYSISTYPE##'
   and analysis_date = (select max(analysis_date) from ai_analysis where analysis_type = '##ANALYSISTYPE##');
"""

AI_SUMMARY = {
    "addresses_balances": {
                                "id": "ai_addresses_balance_summary",
                                "title": "Bitcoin Wallet Balances Over the Last 30 Days",
                                "type": "ai",
                                "indicator": "addresses_balance_summary",
                                "class": "mw-lg-50",
                                "aidate": None,
                                "aicontent": None
    },
    "institutions_etfs": {
                                    "id": "ai_etf_balance_summary",
                                    "title": "Bitcoin Addresses Associated with ETFs Over the Last 30 Days",
                                    "type": "ai",
                                    "indicator": "etf_balance_summary",
                                    "class": "mw-lg-50",
                                    "aidate": None,
                                    "aicontent": None
    },
    "onchain_sopr": {
                                "id": "ai_onchain_sopr_summary",
                                "title": "SOPR Over the Last 30 Days",
                                "type": "ai",
                                "indicator": "onchain_sopr_summary",
                                "class": "mw-lg-50",
                                "aidate": None,
                                "aicontent": None
    },
    "onchain_profitloss": {
                                "id": "ai_onchain_profitloss_summary",
                                "title": "Addresses in Profit and Loss Over the Last 30 Days",
                                "type": "ai",
                                "indicator": "onchain_profitloss_summary",
                                "class": "mw-lg-50",
                                "aidate": None,
                                "aicontent": None
    }                         
}

def get_ai_summary(analysis_type):

    cn = PostgresConn()
    try:
        session = cn.get_cursor_to_pg()       
        session.execute(QUERY.replace('##ANALYSISTYPE##', analysis_type))
        result = session.fetchone()

        cn.close_connection()

        if result is not None:
            return {"date": result[0], "content": result[1]}
        else:
            return None
    except:
        return None


def get_ai_element(chart_type, metric):

    ai_key = chart_type
    if metric is not None:
        ai_key += "_" + metric

    print(ai_key)
    ai_el = AI_SUMMARY.get(ai_key)

    if ai_el is not None:
        ai = get_ai_summary(ai_el['indicator'])
        ai_el['aidate'] = ai['date']
        ai_el['aicontent'] = ai['content']

    return ai_el