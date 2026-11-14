message = input("повідомлення для шифрування: ")
while True:
    try:
        n = int(input("кількість одиниць (N): "))
        break
    except ValueError:
        print("коректне ціле число для.")
        n = n % 26
encrypted_message = ""
for char in message:
    if 'a' <= char <= 'z':
        shifted_char = chr(((ord(char) - ord('a') + n) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        shifted_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
    else:
        shifted_char = char
        encrypted_message += shifted_char

print(f"\nВихідне повідомлення: {message}")
print(f"Кількість (N): {n}")
print(f"Лабораторна робота: {encrypted_message}")