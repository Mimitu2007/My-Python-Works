import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path_keywords = os.path.join(script_dir, 'keywords.txt')
path_web = os.path.join(script_dir, 'web.txt')

print("Створення тестових файлів...")

keywords_content = "python data code programming design"
with open(path_keywords, 'w', encoding='utf-8') as f:
    f.write(keywords_content)
print(f" -> Файл {path_keywords} створено.")

web_content = """https://www.python.org
https://en.wikipedia.org/wiki/Data_science
"""
with open(path_web, 'w', encoding='utf-8') as f:
    f.write(web_content)
print(f" -> Файл {path_web} створено.")
print("-" * 30)

def get_site_text(url):
    """Функція завантажує текст із сайту"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text().lower()
    except Exception as e:
        print(f"Помилка при доступі до {url}: {e}")
    return ""

with open(path_keywords, 'r', encoding='utf-8') as f:
    keywords = f.read().strip().split()

with open(path_web, 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f if line.strip()]

site_counter = 1

for url in urls:
    print(f"Аналізую сайт ({site_counter}/{len(urls)}): {url} ...")
    text = get_site_text(url)
    
    if not text:
        print(" -> Не вдалося отримати текст, пропускаємо.")
        continue
        
    counts = []
    for word in keywords:
        count = text.count(word.lower())
        counts.append(count)
    
    print(f" -> Результати: {counts}")

    plt.figure(figsize=(10, 6))

    bars = plt.bar(keywords, counts, color='orange', edgecolor='black')
    
    plt.xlabel('Ключові слова')
    plt.ylabel('Кількість')
    plt.title(f'Частота слів на сайті:\n{url}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.bar_label(bars)

    filename = os.path.join(script_dir, f'hist_site_{site_counter}.png')
    plt.savefig(filename)
    print(f" -> Графік збережено: {filename}")

    plt.show()
    
    site_counter += 1

print("Роботу завершено!")