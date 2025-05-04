import datetime as dt
from pathlib import Path

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 100,
}

STATUS_COUNT = ('status', 'count')
STATUS_FOOTER = 'total'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
RESULTS_DIR_PATH = BASE_DIR / RESULTS_DIR

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS_SUMMARY_NAME = (
    f'status_summary_{dt.datetime.now().strftime(DATE_FORMAT)}.csv'
)
PEP_NAME = 'pep_%(time)s.csv'

FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    f'{RESULTS_DIR}/{PEP_NAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
