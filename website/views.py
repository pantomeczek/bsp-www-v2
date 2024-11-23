from flask import Blueprint, render_template, request, Flask, redirect, url_for
from flask_login import login_required, current_user
from datetime import timedelta, datetime
from .code.blocks import get_last_blocks
from .code.chartconfig import Chartconfig
from website.code import charts


TYPE_KEY = 'type'
METRIC_KEY = 'metric'
SIZE_KEY = 'size'

DEFAULT_TYPE = 'addresses'
DEFAULT_METRICS = {
    "addresses": "counts",
    "mining": "rewards",
    "supply": None,
    "onchain": "sopr",
    "institutions": "etfs"
}

views = Blueprint('views', __name__)


def get_charts_for_addresses(chart_type, metric, date_of_chart):

    obj = Chartconfig(chart_type, metric, None, None, None).get_details_obj()
    

    

    address_charts = [
        {
            "type":"stats",
            "name": "Distribution of activity",
            "statobj": charts.get_activity_stats()
        }
    ]

    

    if chart_type != 'addresses':
        address_charts=[]

    for i in obj:
        if 'widget_active' in obj[i] and obj[i]['widget_active'] == True:

            url = f"/chart?type={chart_type}&metric={metric}&size={i}" if metric is not None else f"/chart?type={chart_type}&metric={i}"

            mtr = i if metric is None else metric
            smtr = metric if metric is None else i

            inObj = Chartconfig(chart_type, mtr, smtr, None, None)

            if chart_type == 'onchain' and metric == 'sopr':
                chartRes = charts.get_sopr_chart(inObj.get_indicator(inObj.get_precision()), 
                                                 inObj.get_label_with_dma(), 
                                                 inObj.get_value_label(), 
                                                 inObj.get_value_unit(), 
                                                 date_of_chart, 
                                                 340, 
                                                 False)
            elif chart_type == 'onchain' and metric == 'other' and i == 'nupl':
                chartRes = charts.get_nupl_chart(indicator = inObj.get_indicator(inObj.get_precision()), 
                                                 label = inObj.get_label_with_dma(), 
                                                 metric_label = inObj.get_value_label(), 
                                                 metric_unit = inObj.get_value_unit(), 
                                                 filled = False, 
                                                 date_from = date_of_chart, 
                                                 height = 340, 
                                                 show_full = False)
            elif chart_type == 'onchain' and metric == 'other' and i == 'mvrvz':
                chartRes = charts.get_mvrv_chart(date_of_chart, None,340, False)
            else:
                chartRes = charts.get_standard_price_chart(indicator_name = inObj.get_indicator(inObj.get_precision()), 
                                                           indicator_title = inObj.get_label_with_dma(), 
                                                           indicator_value_label = inObj.get_value_label(), 
                                                           indicator_value_unit = inObj.get_value_unit(),
                                                           filled = inObj.is_fillunder(),
                                                           chart_date_from = date_of_chart,
                                                           chart_currency = inObj.get_value_unit(),
                                                           limited_range = None,
                                                           chart_height = 340,
                                                           chart_width = None,
                                                           show_all_tools = False,
                                                           secondary_chart_type = inObj.get_chart_type())
                                
            chartResult = chartRes['chart']
            chartStats = chartRes['stats']

            el = {
                "id": f"chart_{i}",
                "type": "chart",
                "title": obj[i]['label'],
                "href": url,
                "chart": chartResult,
                "stats": chartStats
            }

            address_charts.append(el)

       
    return address_charts

def get_charts(chart_type: str, metric: str, date_of_chart):

    return get_charts_for_addresses(chart_type, metric, date_of_chart)
        

BLKS = get_last_blocks(7)

@views.route('/dashboard')
@views.route('/')
def addresses():

    
    date_of_dashboard = (datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days = 365)).strftime('%Y-%m-%d')

    if TYPE_KEY in request.args:
        content_type = request.args.get(TYPE_KEY)
    else:
        content_type = DEFAULT_TYPE
    
    if METRIC_KEY in request.args:
        content_metric = request.args.get(METRIC_KEY)
    else:
        content_metric = DEFAULT_METRICS[content_type]
    

    if content_type == 'addresses' and content_metric == 'distribution':
        return redirect(url_for('views.chart', type='addresses', metric='distribution'))

    charts = get_charts(content_type, content_metric, date_of_dashboard)
                 
    return render_template("content.html", user=current_user, content_type=content_type, metric=content_metric, blocks=BLKS, charts=charts)


@views.route('/chart')
def chart():

    

    if TYPE_KEY in request.args:
        content_type = request.args.get(TYPE_KEY)
    else:
        content_type = DEFAULT_TYPE
    
    if METRIC_KEY in request.args:
        content_metric = request.args.get(METRIC_KEY)
    else:
        content_metric = DEFAULT_METRICS[content_type]

    if SIZE_KEY in request.args:
        content_size = request.args.get(SIZE_KEY)
    else:
        content_size = DEFAULT_METRICS[content_type]

    if content_type == 'addresses' and content_metric == 'distribution':
        content_size = None

    obj = Chartconfig(content_type, content_metric, content_size, request.args.get("precision"), request.args.get("currency"))
    
    print(f"content_type = {content_type}")
    print(f"content_metric = {content_metric}")
    print(f"content_size = {content_size}")

    stats = None
    limited_range= True if content_type == 'institutions' else False

    if content_type == 'onchain' and content_metric == 'sopr':
        chart = charts.get_sopr_chart(obj.get_indicator(obj.get_precision()), 
                                      obj.get_label_with_dma(), 
                                      "SOPR", 
                                      "BTC", 
                                      obj.get_value_chart_start_date(), 
                                      800, 
                                      True)

    elif content_type == 'addresses' and content_metric == 'distribution':
        chart = charts.get_special_address_price_chart()

    elif content_type == 'onchain' and content_metric == 'other' and content_size == 'nupl':

        chart = charts.get_nupl_chart(obj.get_indicator(obj.get_precision()), 
                                      obj.get_label_with_dma(), 
                                      obj.get_value_label(), 
                                      obj.get_value_unit(),
                                      obj.is_fillunder(),
                                      obj.get_value_chart_start_date(),
                                      chart_currency = obj.get_active_currency(),
                                      limited_range = True,
                                      secondary_chart_type = obj.get_chart_type())

    elif content_type == 'onchain' and content_metric == 'other' and content_size == 'mvrvz':
        chart = charts.get_mvrv_chart()                                      
    else:
        
        chart = charts.get_standard_price_chart(indicator_name = obj.get_indicator(obj.get_precision()), 
                                                indicator_title = obj.get_label_with_dma(), 
                                                indicator_value_label = obj.get_value_label(), 
                                                indicator_value_unit = obj.get_value_unit(),
                                                filled = obj.is_fillunder(),
                                                chart_date_from = obj.get_value_chart_start_date(),
                                                chart_currency = obj.get_active_currency(),
                                                secondary_chart_type = obj.get_chart_type(),
                                                limited_range=True)
        

    result_stats = chart['stats']
    result_chart = chart['chart']

    description_file_name = f"{content_type}_{obj.get_metric()}"
    
    if content_size is not None and content_type not in ['addresses']:
        description_file_name = f"{description_file_name}_{content_size}"

    return render_template('charts.html',    graph = result_chart,
                                             stats = result_stats,
                                             user = current_user,
                                             title = obj.get_label(),
                                             label = obj.get_submetric(),
                                             metric = obj.get_metric(),
                                             module = "chart",
                                             content_type=content_type,
                                             url = f"/chart?type={content_type}&metric={obj.get_metric()}&size={obj.get_submetric()}",
                                             precision_selector_enabled = obj.is_precision_selector_enabled(),
                                             currency_selector_enabled = obj.is_currency_selector_enabled(),
                                             precision = obj.get_active_precision(),
                                             currency = obj.get_active_currency(),
                                             blocks = BLKS,
                                             description_label = description_file_name)