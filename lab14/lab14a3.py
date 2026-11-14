import random
import string

def create_nested_list(rows, cols, min_val, max_val):
    """
    Створює вкладений список (матрицю) розміром rows x cols
    з випадкових цілих чисел у діапазоні [min_val, max_val].
    """
    nested_list = [
        [random.randint(min_val, max_val) for _ in range(cols)]
        for _ in range(rows)
    ]
    return nested_list

def create_list_of_strings(*args):
    """
    Створює список рядків з випадкових символів, використовуючи *args.
    
    Приймає змінну кількість аргументів:
    - 2 аргументи: (кількість_рядків, довжина_рядка) -> стандартний алфавіт.
    - 3 аргументи: (кількість_рядків, довжина_рядка, алфавіт) -> заданий алфавіт.
    """
    
    if len(args) == 2:
        num_strings, string_length = args
        alphabet = string.ascii_letters + string.digits
    elif len(args) == 3:
        num_strings, string_length, alphabet = args
    else:
        raise ValueError("Очікується 2 або 3 аргументи: (кількість рядків, довжина рядка, [алфавіт])")

    list_of_strings = []
    for _ in range(num_strings):
        random_string = ''.join(random.choice(alphabet) for _ in range(string_length))
        list_of_strings.append(random_string)
        
    return list_of_strings