import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

base_dir = os.path.dirname(os.path.abspath(__file__))
countries_path = os.path.join(base_dir, 'countries.txt')
web_path = os.path.join(base_dir, 'web.txt')
output_path = os.path.join(base_dir, 'top_countries.json')

try:
    with open(countries_path, 'r', encoding='utf-8') as f:
        countries = [line.strip() for line in f if line.strip()]
    
    with open(web_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    if not countries or not urls:
        print("Помилка: Файли countries.txt або web.txt порожні. Заповніть їх даними!")
        countries = [] 
        urls = []
        
except FileNotFoundError:
    print("Помилка: Файли countries.txt або web.txt не знайдено.")
    countries = [] 
    urls = []

if not urls:
    print("Сканування пропущено, оскільки список URL-адрес порожній.")
else:
    all_counts = Counter()

    print("Початок сканування веб-сторінок...")

    for url in urls:

        try:
            req = requests.get(url, headers=headers, timeout=10)

            if req.status_code == 200:
                print(f"Успішно завантажено: {url}")
                
                soup = BeautifulSoup(req.text, "html.parser")
                text_content = soup.get_text()
                lower_text = text_content.lower()
                
                for country in countries:
                    count = len(re.findall(r'\b' + re.escape(country.lower()) + r'\b', lower_text))
                    if count > 0:
                        all_counts[country] += count
            else:
                print(f"Помилка доступу ({req.status_code}) до: {url}")
                
        except requests.exceptions.RequestException as e:
            print(f"Помилка запиту до {url}: {e}")

    top_3_countries = dict(all_counts.most_common(3))

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(top_3_countries, f, ensure_ascii=False, indent=4)

    print("-" * 40)
    print(f"Топ-3 країни: {top_3_countries}")
    print(f"Результат збережено у файл: {output_path}")
    print("-" * 40)