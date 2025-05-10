import csv
import os
import random

def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames or []
        data = [row for row in reader]
    return headers, data

def Show(headers, data, output_type='top', rows=5, separator=','):
    if not data:
        print("Данные не найдены")
        return
    
    total_rows = len(data)
    rows = min(rows, total_rows)
    
    if rows < 5 and rows != total_rows:
        print(f"Запрошено {rows} строк, но в данных всего {total_rows} строк")
    
    if output_type == 'top':
        rows_to_show = data[:rows]
    elif output_type == 'bottom':
        rows_to_show = data[-rows:]
    elif output_type == 'random':
        rows_to_show = random.sample(data, rows)
    else:
        print(f"Неизвестный тип вывода: {output_type}. Используется 'top'")
        rows_to_show = data[:rows]
    
    col_widths = {header: len(header) for header in headers}
    for row in rows_to_show:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(str(row.get(header, ''))))
    
    header_line = separator.join([f"{header:<{col_widths[header]}}" for header in headers])
    print(header_line)
    print(separator.join(['-' * col_widths[header] for header in headers]))
    
    for row in rows_to_show:
        row_line = separator.join([f"{row.get(header, ''):<{col_widths[header]}}" for header in headers])
        print(row_line)

def Info(headers, data):
    if not data:
        print("Данные не найдены")
        return
    
    rows = len(data)
    cols = len(headers)
    print(f"{rows}x{cols}")
    
    for header in headers:
        non_empty = 0
        types = set()
        
        for row in data:
            value = row.get(header, '')
            if value.strip():
                non_empty += 1

            non_empty += 1
            if value.lstrip('-').isdigit():
                types.add('int')
            elif value.lstrip('-').replace('.', '', 1).isdigit():
                types.add('float')
        
        type_str = '/'.join(sorted(types)) if types else 'string'
        print(f"{header} {non_empty} {type_str}")

def DelNaN(headers, data):
    if not data:
        return data
    
    return [row for row in data if all(row.get(header, '').strip() for header in headers)]

def MakeDS(headers, data):
    if not data:
        print("Данные не найдены")
        return
    
    base_dir = "workdata"
    learning_dir = os.path.join(base_dir, "Learning")
    testing_dir = os.path.join(base_dir, "Testing")
    
    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    shuffled_data = random.sample(data, len(data))

    split_idx = int(0.7 * len(shuffled_data))
    train_data = shuffled_data[:split_idx]
    test_data = shuffled_data[split_idx:]

    train_path = os.path.join(learning_dir, "train.csv")
    with open(train_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(train_data)

    test_path = os.path.join(testing_dir, "test.csv")
    with open(test_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(test_data)
    
    print(f"Данные успешно разделены и сохранены в {base_dir}/")

if __name__ == "__main__":
    filename = input("Введите имя CSV файла: ")
    headers, data = load_csv(filename)
    
    while True:
        print("1. Show() - показать данные")
        print("2. Info() - показать информацию о данных")
        print("3. DelNaN() - удалить строки с пустыми значениями")
        print("4. MakeDS() - разделить данные на обучающую и тестовую выборки")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            output_type = input("Тип вывода (top/bottom/random, по умолчанию top): ") or 'top'
            rows = input("Количество строк (по умолчанию 5): ")
            rows = int(rows) if rows.isdigit() else 5
            separator = input("Разделитель (по умолчанию ','): ") or ','
            Show(headers, data, output_type, rows, separator)
        
        elif choice == '2':
            Info(headers, data)
        
        elif choice == '3':
            data = DelNaN(headers, data)
            print("Пустые строки удалены")
        
        elif choice == '4':
            MakeDS(headers, data)
        
        elif choice == '5':
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
