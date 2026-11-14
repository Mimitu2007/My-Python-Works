try:
    with open(C:\Users\Kotaro\Desktop\laboratoru\lab11\lab\data.txt, "r") as f:
        max_y = float("-inf")
        x_max = 0.0

        sum_y = 0.0
        count = 0

        for line in f:
            parts = line.split()
            if len(parts) == 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])

                    if y > max_y:
                        max_y = y
                        x_max = x

                    sum_y += y
                    count += 1
                except ValueError:
                    continue
            
    if count > 0:
        max_point = (x_max, max_y)
        average_y = sum_y / count
        print(f"1) Точка максимуму (x0; y0): {max_point}")
        print(f"2) Середнє значення функції: {average_y:.4f}")
    else:
        print("Файл порожній або містить некоректні дані.")

except FileNotFoundError:
    print("Помилка: Файл 'data.txt' не знайдено.")