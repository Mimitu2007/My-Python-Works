import random
import string

len_digits = int(input("Введіть довжину рядка цифр: "))
len_chars = int(input("Введіть довжину рядка літер: "))

digits = [random.choice(string.digits) for _ in range(len_digits)]
line1 = ",".join(digits) 

chars = [random.choice(string.ascii_letters) for _ in range(len_chars)]
line2 = "".join(chars) 
file_name = "random_output.txt"
try:
    with open(file_name, "w") as f:
        f.write("Рядок випадкових цифр:\n")
        f.write(line1 + "\n") 
        
        f.write("Рядок випадкових символів:\n")
        f.write(line2 + "\n")

    print(f"\nДані успішно записано у файл '{file_name}'.")

except IOError:
    print("Виникла помилка під час запису у файл.")