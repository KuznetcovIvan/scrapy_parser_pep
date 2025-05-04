# Парсер документов PEP
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5-green)

Это парсер на Python, основанный на фреймворке Scrapy и предназначенный для извлечения и обработки данных с официального сайта [предложений по улучшению Python (PEP)](https://peps.python.org/).

#### Является переработанной версией парсера на библиотеке **BeautifulSoup** с которой можно ознакомится [тут](https://github.com/KuznetcovIvan/bs4_parser_pep).

В функционал входит
- парсинг данных обо всех документах PEP,
- обработка и вывод количества PEP в каждом статусе, а также общего количества PEP.
___

## Технологический стек

- Python 3.9: Язык программирования.
- Scrapy 2.5.1: Фреймворк для веб-парсинга.
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

Просмотреть справку по Scrapy `scrapy crawl --help`
___
### Автор: [Иван Кузнецов](https://github.com/KuznetcovIvan) 