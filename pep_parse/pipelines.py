import csv
from collections import defaultdict

from .settings import (
    RESULTS_DIR_PATH, STATUS_COUNT, STATUS_FOOTER, STATUS_SUMMARY_NAME
)


class PepParsePipeline:
    def __init__(self):
        RESULTS_DIR_PATH.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_summary = defaultdict(int)

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            RESULTS_DIR_PATH / STATUS_SUMMARY_NAME, 'w', encoding='utf-8'
        ) as file:
            csv.writer(
                file, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows((
                STATUS_COUNT,
                *self.status_summary.items(),
                (STATUS_FOOTER, sum(self.status_summary.values()))
            ))
