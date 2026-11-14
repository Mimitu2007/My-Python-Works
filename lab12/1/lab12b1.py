import pickle
FILE = 'set_data.bin'
f = open(FILE, 'rb')
loaded_set = pickle.load(f)
f.close()
print(f"Зчитана множина з файлу '{FILE}':")
print(loaded_set)