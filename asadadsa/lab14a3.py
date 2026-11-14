import math

def check_function_graph(*points):
    """
    Перевіряє, чи належать задані точки (x, y) графіку функції f(x) = x^2 - x + sin(x).
    Приймає змінну кількість кортежів (пар) точок, наприклад: (x1, y1), (x2, y2), ...
    """
    results = {}
    
    def f(x):
        return x**2 - x + math.sin(x)
        
    for i, point in enumerate(points):
        if len(point) != 2:
            results[f"Точка {i+1} ({point})"] = "Помилка: Не є парою (x, y)"
            continue
            
        x, y_given = point
        y_calculated = f(x)
        
        if math.isclose(y_given, y_calculated):
            results[f"Точка {i+1} ({x}, {y_given})"] = "Належить графіку"
        else:
            results[f"Точка {i+1} ({x}, {y_given})"] = (f"НЕ належить (Очікуване Y: {y_calculated:.4f}, "
                                                        f"Задане Y: {y_given:.4f})")
    return results

def count_words_in_strings(*strings):
    """
    Підраховує загальну кількість слів у всіх переданих рядках.
    Приймає змінну кількість рядків.
    """
    total_word_count = 0
    
    for current_string in strings:
        words = current_string.split()
        word_count = len(words)
        total_word_count += word_count
        print(f"-> Рядок '{current_string[:20]}...': {word_count} слів.")
        
    return total_word_count