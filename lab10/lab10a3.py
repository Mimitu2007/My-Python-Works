country_areas = {
    "Норвегія": 385.2,
    "Швеція": 450.3,
    "Фінляндія": 338.4,
    "Данія": 43.1,
    "Бельгія": 30.5
}
print("--- Площі країн (тис. км²) ---")
for key in country_areas:
    value = country_areas[key]
    print(f"{key}: {value}")
search_country = input("\nВведіть країну, щоб дізнатися її площу: ")
if search_country in country_areas:
    area = country_areas[search_country]
    print(f"Площа {search_country} становить {area} тис. км².")
else:
    print(f"Країна '{search_country}' не знайдена.")