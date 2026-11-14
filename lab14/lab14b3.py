import lab14a3

print("### Створення вкладеного списку (Матриця 3x4 з чисел [10, 50]) ###")
try:
    matrix = lab14a3.create_nested_list(3, 4, 10, 50)
    for row in matrix:
        print(row)
except Exception as e:
    print(f"Помилка при створенні вкладеного списку: {e}")

print("\n" + "="*30 + "\n")

print("### Створення списку 5 рядків довжиною 6 (стандартний алфавіт) ###")
try:
    strings1 = lab14a3.create_list_of_strings(5, 6)
    print(strings1)
except Exception as e:
    print(f"Помилка при створенні списку рядків 1: {e}")

print("\n")

print("### Створення списку 3 рядків довжиною 10 (алфавіт: 'aeiou') ###")
try:
    custom_alphabet = 'aeiou'
    strings2 = lab14a3.create_list_of_strings(3, 10, custom_alphabet)
    print(strings2)
except Exception as e:
    print(f"Помилка при створенні списку рядків 2: {e}")