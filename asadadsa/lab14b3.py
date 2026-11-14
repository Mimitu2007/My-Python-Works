import lab14a3

print("="*40)
print("1. ПЕРЕВІРКА НАЛЕЖНОСТІ ТОЧОК ГРАФІКУ (f(x) = x^2 - x + sin(x))")
print("="*40)

points_to_check = [
    (0.5, 0.22957),
    (2, 3.0),
    (3, 8.0)
]

results = lab14a3.check_function_graph(*points_to_check)
for point, status in results.items():
    print(f"{point}: {status}")

print("\n" + "="*40)
print("2. ПІДРАХУНОК КІЛЬКОСТІ СЛІВ У РЯДКАХ")
print("="*40)

total_words = lab14a3.count_words_in_strings(
    "Це перший рядок.",
    "Це другий, більш довгий рядок з великою кількістю слів для перевірки.",
    "Третій.",
    "І четвертий рядок, який містить лише 4 слова."
)

print(f"\nЗагальна кількість слів у всіх рядках: {total_words}")