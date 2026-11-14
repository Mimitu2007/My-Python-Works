word_list = [
    "apple", "banana", "cherry", "Strawberry", "elderberry", "fig",
    "grape", "honeydew", "apple", "kiwi", "banana", "lemon"
]
from collections import Counter
counts = Counter(word_list)
repeated = [word for word, count in counts.items() if count > 1]
shortest_word = min(word_list, key=len)
total_s_count = 0
for word in word_list:
    total_s_count += word.lower().count('s')
print("1. Повторювані слова:", repeated)
print("2. Найкоротше слово:", shortest_word)
print("3. Загальна кількість літер 's':", total_s_count)
