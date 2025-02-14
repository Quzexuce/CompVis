import random

def вывести_слова_в_случайном_порядке(список_слов):
    # Удаляем дубликаты из списка слов, чтобы слова не повторялись
    уникальные_слова = list(set(список_слов))
    
    # Перемешиваем уникальные слова случайным образом
    random.shuffle(уникальные_слова)
    
    # Выводим перемешанные слова
    print("Слова в случайном порядке:")
    for слово in уникальные_слова:
        print(слово)

# Пример списка слов
список_слов = ["яблоко", "банан", "апельсин", "вишня", "яблоко", "персик", "апельсин"]

# Запуск функции
вывести_слова_в_случайном_порядке(список_слов)
