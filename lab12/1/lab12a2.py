import shelve
FILE = 'street_data.dat'
street_data = {
    'Шевченка': 180,
    'Центральна': 350, 
    'Лесі Українки': 95,
    'Космонавтів': 210,
    'Перемоги': 310,   
    'Садова': 65,
}
print(f"Створений словник для запису: {street_data}")
with shelve.open(FILE, 'c') as db:
    for street, count in street_data.items():
        db[street] = count

print(f"\nСловник успішно збережено у базу даних '{FILE}'.")