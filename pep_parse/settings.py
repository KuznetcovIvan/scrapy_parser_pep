import datetime as dt
from pathlib import Path

BOT_NAME = 'pep_parse'

ALLOWED_DOMAIN = 'peps.python.org'
START_URL = f'https://{ALLOWED_DOMAIN}/'

SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 100,
}

NUMBER = 'number'
NAME = 'name'
STATUS = 'status'
STATUS_COUNT = (STATUS, 'count')

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

STATUS_SUMMARY_NAME = (
    f'status_summary_{dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
)
PEP_NAME = 'pep_%(time)s.csv'

FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    f'{RESULTS_DIR}/{PEP_NAME}': {
        'format': 'csv',
        'fields': [NUMBER, NAME, STATUS],
        'overwrite': True
    }
}
