data = ["1.0 5.2", "2.5 8.5", "4.5 9.8", "5.0 7.5"]

max_y = -999999
x_max = 0
sum_y = 0
count = 0

for line in data:
    x, y = map(float, line.split())

    if y > max_y:
        max_y = y
        x_max = x

    sum_y += y
    count += 1

if count > 0:
    print(f"1) Точка максимуму (X; Y): ({x_max}, {max_y})")
    print(f"2) Середнє значення Y: {sum_y / count:.2f}")
else:
    print("Немає даних.")