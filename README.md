# CSV Processor

## Описание
Скрипт на Python для фильтрации и агрегации данных из CSV-файла. Работает через аргументы командной строки.

## Установка

```bash
pip install tabulate
```

## Примеры запуска

Фильтрация:
```bash
python script.py --file phones.csv --where "price>500"
```

Агрегация:
```bash
python script.py --file phones.csv --aggregate "price=avg"
```

Фильтрация и агрегация:
```bash
python script.py --file phones.csv --where "brand=xiaomi" --aggregate "price=avg"
```

## Тестирование

```bash
pytest test_script.py
```

## Ограничения
- Только стандартная библиотека (csv, argparse)
- Для вывода используется `tabulate`
- Без использования pandas

## Автор
Кандидат на позицию Python Junior
