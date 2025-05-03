# Парсер документов PEP

Это парсер на Python, основанный на фреймворке Scrapy и предназначенный для извлечения и обработки данных с официального сайта [предложений по улучшению Python (PEP)](https://peps.python.org/).

В функционал входит
- парсинг данных обо всех документах PEP,
- обработка и вывод количества PEP в каждом статусе, а также общего количества PEP.
___

## Установка

- Клонируйте проект с [репозитория](https://github.com/KuznetcovIvan/scrapy_parser_pep.git) `git clone https://github.com/KuznetcovIvan/scrapy_parser_pep.git`.
- Находясь в корне проекта создайте и активируйте виртуальное окружение `python -m venv venv`, `source/venv/Script/activate`
(`python3 -m venv venv`, `source venv/bin/activate` для Linux / macOS).
- Установите зависимости из файла requirements.txt `pip install -r requirements.txt`.

___

## Использование

Находясь в корне проекта, запустите парсер командой `scrapy crawl pep`.

Парсер сохранит данные в файлы .csv в директорию `results/`:
- файл со списком PEP (содержит колонки: number, name, status),
- файл со сводкой по статусам (status, count)
___
### Автор: [Иван Кузнецов](https://github.com/KuznetcovIvan) 