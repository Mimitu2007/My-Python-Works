import json
FILE_NAME = 'goods_prices.json'
goods_data = {
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 6500,
    "Webcam": 1200,
    "Headphones": 2300
}

print("Створений словник товарів:")
print(goods_data)
with open(FILE_NAME, 'w', encoding='utf-8') as write_file:
    json.dump(goods_data, write_file, indent=4) 

print(f"\nСловник успішно збережено у файл '{FILE_NAME}'.")