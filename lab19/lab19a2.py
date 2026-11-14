import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path_input = os.path.join(script_dir, 'input.txt')
path_json = os.path.join(script_dir, 'perimeter.json')

print("Створення файлу input.txt...")

input_content = """1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""
with open(path_input, 'w', encoding='utf-8') as f:
    f.write(input_content)

print("Читання матриці...")
df = pd.read_csv(path_input, sep='\s+', header=None)
print("Вхідна матриця:")
print(df.values)

top = df.iloc[0, :].tolist()

right = df.iloc[1:-1, -1].tolist()

bottom = df.iloc[-1, :].tolist()[::-1]

left = df.iloc[1:-1, 0].tolist()[::-1]

all_perimeter = top + right + bottom + left

s = pd.Series(all_perimeter)

print("\nЧисла по периметру:")
print(s.values)

s.to_json(path_json, orient='values')
print(f"\nДані збережено у файл: {path_json}")