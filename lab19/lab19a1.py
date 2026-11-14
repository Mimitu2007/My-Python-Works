import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path_polygon = os.path.join(script_dir, 'polygon.csv')
path_sides = os.path.join(script_dir, 'sides.csv')

print("Створення файлу polygon.csv...")
polygon_content = """Point,X,Y
A,0,0
B,0,3
C,4,0
"""
with open(path_polygon, 'w', encoding='utf-8') as f:
    f.write(polygon_content)

print("Читання даних...")
df = pd.read_csv(path_polygon)
print(df)

segments = []
lengths = []
n = len(df)

for i in range(n):
    p1 = df.iloc[i]
    p2 = df.iloc[(i + 1) % n]   
    
    seg_name = f"{p1['Point']}{p2['Point']}"
    
    dist = np.sqrt((p2['X'] - p1['X'])**2 + (p2['Y'] - p1['Y'])**2)
    
    segments.append(seg_name)
    lengths.append(round(dist, 2))

df_res = pd.DataFrame({'Segment': segments, 'Length': lengths})

print("\nРезультат:")
print(df_res)

df_res.to_csv(path_sides, index=False)
print(f"\nДані збережено у файл: {path_sides}")