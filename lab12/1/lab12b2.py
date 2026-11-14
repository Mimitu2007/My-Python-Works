import shelve
FILE = 'street_data.dat'
TOP_N = 2
with shelve.open(FILE, 'r') as db:
    data_list = list(db.items())
    sorted_streets = sorted(data_list, key=lambda item: item[1], reverse=True)
    top_streets = sorted_streets[:TOP_N]
    print(f"Зчитані дані та відсортовані за кількістю будинків.")
    print(f"\n{TOP_N} вулиці, які мають найбільше будинків:")
    for street, count in top_streets:
        print(f"- {street}: {count} будинків")