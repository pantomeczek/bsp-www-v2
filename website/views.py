from flask import Blueprint, render_template, request, Flask
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
    "mining": "rewards"
}

views = Blueprint('views', __name__)


def get_charts_for_addresses(chart_type, metric, date_of_chart):

    obj = Chartconfig(chart_type, metric, None, None, None).get_details_obj()
    
    address_charts = [
        {
            "type":"stats",
            "statobj": charts.get_addresses_perc_details(30)
        }
    ]

    for i in obj:
        if 'widget_active' in obj[i] and obj[i]['widget_active'] == True:
            el = {
                "id": f"chart_{i}",
                "type": "chart",
                "title": obj[i]['label'],
                "href": f"/chart?type={chart_type}&metric={metric}&size={i}",
                "chart": charts.get_standard_price_chart(indicator_name = obj[i]['indicators']['normal'], 
                                                         indicator_title = obj[i]['value_label'], 
                                                         indicator_value_label = obj[i]['value_label'], 
                                                         indicator_value_unit = obj[i]['value_unit'],
                                                         filled = False,
                                                         chart_date_from = date_of_chart,
                                                         chart_currency = 'BTC',
                                                         limited_range = None,
                                                         chart_height = 400,
                                                         chart_width = None,
                                                         show_all_tools = False)
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

    obj = Chartconfig(content_type, content_metric, content_size, request.args.get("precision"), request.args.get("currency"))
    
    chart = graph=charts.get_standard_price_chart(indicator_name = obj.get_indicator(obj.get_precision()), 
                                                  indicator_title = obj.get_label_with_dma(), 
                                                  indicator_value_label = obj.get_value_label(), 
                                                  indicator_value_unit = obj.get_value_unit(),
                                                  filled = obj.is_fillunder(),
                                                  chart_date_from = obj.get_value_chart_start_date(),
                                                  chart_currency = obj.get_active_currency())


    return render_template('charts.html',    graph = chart,
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
                                             description_label = "addresses_" + obj.get_metric())