import csv
from collections import defaultdict

from .settings import (
    BASE_DIR, RESULTS_DIR, STATUS, STATUS_COUNT, STATUS_SUMMARY_NAME
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_summary = defaultdict(int)

    def process_item(self, item, spider):
        self.status_summary[item[STATUS]] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / STATUS_SUMMARY_NAME
        with open(file_path, 'w', encoding='utf-8') as file:
            csv.writer(file, dialect=csv.unix_dialect).writerows([
                STATUS_COUNT,
                *self.status_summary.items(),
                ('total', sum(self.status_summary.values()))
            ])
