nums = [23, 45, 67, 89, 12, 34]

remainders = [num % 7 for num in nums]
max_remainder = max(remainders)

print("Список чисел:", nums)
print("Остачі від ділення на 7:", remainders)
print("Найбільша остача:", max_remainder)
