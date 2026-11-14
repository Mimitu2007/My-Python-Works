import requests
from bs4 import BeautifulSoup
import json
import re
import os 

search_word = "Ukraine"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

news_urls = [
    'https://www.bbc.com/news/world/europe',
    'https://edition.cnn.com/',
    'https://www.nytimes.com/'
]

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'news.json'
output_path = os.path.join(base_dir, file_name)

results = {}

print("Початок сканування новинних сторінок...")

for url in news_urls:
    try:
        req = requests.get(url, headers=headers, timeout=10)
        
        if req.status_code == 200:
            print(f"Успішно завантажено: {url}")
            
            soup = BeautifulSoup(req.text, "html.parser")
            text_content = soup.get_text()
            lower_text = text_content.lower()
            lower_search_word = search_word.lower()
            count = len(re.findall(r'\b' + lower_search_word + r'\b', lower_text))
            
            results[url] = {
                "word": search_word,
                "count": count
            }
        else:
            print(f"Помилка доступу ({req.status_code}) до: {url}")
            results[url] = {"error": f"Access denied. Status code: {req.status_code}"}
            
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту до {url}: {e}")
        results[url] = {"error": f"Request failed: {e}"}
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("-" * 40)
print(f"Результат підрахунку: {results}")
print(f"Результат збережено у файл: {output_path}")
print("-" * 40)