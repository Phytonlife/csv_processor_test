import csv
import argparse
from tabulate import tabulate

# Чтение CSV-файла
def read_csv(file_path: str) -> list[dict]:
    with open(file_path, newline='', encoding='utf-8') as f:

        return list(csv.DictReader(f))  # Чтение в виде списка словарей

# Фильтрация данных
def filter_data(data: list[dict], condition: str) -> list[dict]:
    column, operator, value = parse_condition(condition)
    result = []
    for row in data:
        cell = row[column]
        try:
            # Пробуем преобразовать к числу
            cell = float(cell)
            value = float(value)
        except ValueError:
            pass  # Если не число, оставляем как есть
        # Сравнение в зависимости от оператора
        if operator == '=' and cell == value:
            result.append(row)
        elif operator == '>' and cell > value:
            result.append(row)
        elif operator == '<' and cell < value:
            result.append(row)
    return result

# Агрегация: avg, min, max
def aggregate_data(data: list[dict], instruction: str) -> float:
    print(instruction)
    column, op = instruction.split('=')
    values = [float(row[column]) for row in data]
    if op == 'avg':
        return sum(values) / len(values)
    elif op == 'min':
        return min(values)
    elif op == 'max':
        return max(values)
    else:
        raise ValueError("Неизвестная операция")

# Парсинг условия фильтрации
def parse_condition(cond: str):
    for op in ['>=', '<=', '>', '<', '=']:
        if op in cond:
            col, val = cond.split(op)
            return col.strip(), op, val.strip()
    raise ValueError("Неверный формат фильтрации")

# Основная функция запуска
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)  # путь к CSV
    parser.add_argument('--where')  # фильтрация
    parser.add_argument('--aggregate')  # агрегация
    args = parser.parse_args()

    data = read_csv(args.file)

    if args.where:
        data = filter_data(data, args.where)
        print(tabulate(data, headers="keys"))

    if args.aggregate:
        result = aggregate_data(data, args.aggregate)
        print(f"Результат агрегации: {result}")

if __name__ == '__main__':
    main()
