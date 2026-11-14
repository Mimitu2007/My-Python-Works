import sqlite3
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'computer_store.db')

def init_db():
    """Створює базу даних та наповнює її, якщо вона порожня"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL,
            quantity INTEGER
        )
    ''')
    
    cursor.execute('SELECT count(*) FROM products')
    if cursor.fetchone()[0] == 0:
        data = [
            ('Laptop Dell XPS', 'Laptops', 25000, 5),
            ('MacBook Air', 'Laptops', 40000, 3),
            ('HP Pavilion', 'Laptops', 22000, 7),
            ('Logitech Mouse', 'Accessories', 1200, 50),
            ('Razer Keyboard', 'Accessories', 3500, 20),
            ('Samsung Monitor', 'Monitors', 8000, 10),
            ('LG Ultrawide', 'Monitors', 12000, 4),
            ('USB Cable', 'Cables', 200, 100),
            ('HDMI Cable', 'Cables', 350, 40),
            ('GeForce RTX 3060', 'Components', 15000, 8),
            ('Intel Core i5', 'Components', 7000, 15)
        ]
        cursor.executemany('INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)', data)
        conn.commit()
        print("Базу даних створено та наповнено.")
    
    conn.close()

def fetch_all():
    """Отримує всі записи з БД"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_by_category(category):
    """Шукає записи за категорією"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE category LIKE ?", ('%' + category + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_stats():
    """Отримує дані для графіка: категорія -> кількість товарів"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(quantity) FROM products GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    return rows

def show_data(data):
    """Виводить дані у віджет Listbox"""
    listbox.delete(0, tk.END) 
    for row in data:
        item = f"{row[0]} | {row[1]} | {row[2]} | {row[3]} грн | {row[4]} шт."
        listbox.insert(tk.END, item)

def on_show_all():
    rows = fetch_all()
    show_data(rows)

def on_search():
    category = entry_search.get()
    if category:
        rows = search_by_category(category)
        show_data(rows)
    else:
        messagebox.showwarning("Увага", "Введіть категорію для пошуку!")

def on_show_chart():
    """Будує графік"""
    stats = get_stats()
    
    if not stats:
        return

    categories = [row[0] for row in stats]
    quantities = [row[1] for row in stats]
    
    plt.figure(figsize=(8, 5))
    plt.bar(categories, quantities, color='skyblue', edgecolor='black')
    plt.xlabel('Категорія')
    plt.ylabel('Загальна кількість (шт.)')
    plt.title('Кількість товарів на складі по категоріях')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    init_db()

    root = tk.Tk()
    root.title("Лабораторна №20 (Варіант 19) - Магазин")
    root.geometry("600x450")

    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    lbl_search = tk.Label(frame_top, text="Пошук за категорією:")
    lbl_search.pack(side=tk.LEFT, padx=5)

    entry_search = tk.Entry(frame_top)
    entry_search.pack(side=tk.LEFT, padx=5)

    btn_search = tk.Button(frame_top, text="Знайти", command=on_search)
    btn_search.pack(side=tk.LEFT, padx=5)

    btn_all = tk.Button(frame_top, text="Показати всі", command=on_show_all)
    btn_all.pack(side=tk.LEFT, padx=5)

    listbox = tk.Listbox(root, width=80, height=15)
    listbox.pack(pady=10, padx=10)

    btn_chart = tk.Button(root, text="Побудувати діаграму кількості", command=on_show_chart, bg="orange")
    btn_chart.pack(pady=10)

    on_show_all()

    root.mainloop()