import csv
FILE_NAME = 'phone_prices.csv'
TOP_N = 2
all_phones = []
try:
    with open(FILE_NAME, 'r', newline='', encoding='utf-8') as f_obj:
        reader = csv.DictReader(f_obj, delimiter=';')
        
        for row in reader:
            row['Price'] = int(row['Price'])
            all_phones.append(row)

except FileNotFoundError:
    print(f"Помилка: Файл '{FILE_NAME}' не знайдено.")
    exit()

if not all_phones:
    print("Файл порожній. Немає даних для аналізу.")
    exit()
sorted_phones = sorted(all_phones, key=lambda item: item['Price'], reverse=True)
top_2_phones = sorted_phones[:TOP_N]
print(f"Загальна кількість моделей: {len(all_phones)}.")
print(f"\n{TOP_N} найдорожчі моделі мобільних телефонів:")
for phone in top_2_phones:
    print(f"- {phone['Model']}: {phone['Price']} UAH")