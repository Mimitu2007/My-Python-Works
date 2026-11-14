s = input("Введіть рядок, що містить літери та цифри (мінімум 3 цифри): ")
digit_indices = []
for index, char in enumerate(s):
    if char.isdigit():
        digit_indices.append(index)

if len(digit_indices) < 3:
    print("Помилка: Рядок має містити щонайменше три цифри.")
else:
    first_digit_index = digit_indices[0]
    third_digit_index = digit_indices[2]
    part1 = s[:first_digit_index + 1]
    part2 = s[third_digit_index:]
    result_string = part1 + part2

    print(f"\nВихідний рядок: {s}")
    print(f"Індекс першої цифри ({s[first_digit_index]}): {first_digit_index}")
    print(f"Індекс третьої цифри ({s[third_digit_index]}): {third_digit_index}")
    print(f"Результат: {result_string}")