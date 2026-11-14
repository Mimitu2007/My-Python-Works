import pickle
set_M = {10, 25, 42, 5, 88, 9, 'A', 'B', 'C', 'X', 'Y', 'Z'}
FILE = 'set_data.bin'
print(f"Множина для запису: {set_M}")
f = open(FILE, 'wb')
pickle.dump(set_M, f)
f.close()
print(f"Множина успішно збережена у файл '{FILE}'.")
