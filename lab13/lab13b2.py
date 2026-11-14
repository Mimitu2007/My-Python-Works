import json
FILE_NAME = 'goods_prices.json'
with open(FILE_NAME, 'r', encoding='utf-8') as read_file:
    data = json.load(read_file)  
print(f"Зчитані відомості про товари з файлу '{FILE_NAME}':")
if data:
    print("\n--- НАЗВА ТОВАРУ та ЦІНА ---")
    for item_name, price in data.items():
        print(f"Товар: {item_name}, Ціна: {price} UAH")
else:
    print("Файл JSON не містить даних для виведення.")