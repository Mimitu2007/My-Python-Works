import csv
PHONE_PRICES = {
    'Samsung Galaxy S23': 32000,
    'iPhone 15 Pro': 48000,  
    'Xiaomi Redmi 12': 8500,
    'Google Pixel 8': 25000,
    'Motorola Edge 40': 15000,
    'OnePlus 11': 28000,
    'Nokia G42': 7000,
    'Oppo Reno 10': 12000,
    'iPhone 14': 35000,      
    'Sony Xperia 5': 18000,
    'Honor 90': 14000,
    'Samsung A54': 11000
}
FILE_NAME = 'phone_prices.csv'
FIELDNAMES = ['Model', 'Price']

print(f"Створений словник цін ({len(PHONE_PRICES)} моделей).")
with open(FILE_NAME, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES, delimiter=';')
    writer.writeheader()
    for model, price in PHONE_PRICES.items():
        writer.writerow({'Model': model, 'Price': price})

print(f"Дані успішно збережено у файл '{FILE_NAME}'.")