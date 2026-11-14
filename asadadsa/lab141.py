def sum_even_indexed_recursive(data_list, index=0):
    """
    Обчислює суму елементів списку, що мають парні індекси (0, 2, 4...).
    """
    if index >= len(data_list):
        return 0
    
    current_value = data_list[index]
    
    remaining_sum = sum_even_indexed_recursive(data_list, index + 2)
    
    return current_value + remaining_sum

my_list = [10, 2, 30, 4, 50, 6, 70, 8]

result_sum = sum_even_indexed_recursive(my_list)
print(f"Список: {my_list}")
print(f"Сума елементів з парними індексами (10+30+50+70): {result_sum}")