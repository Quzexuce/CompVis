def кто_твой_папа_и_дед(имя):
    # Расширенный словарь, включающий несколько поколений
    семья = {
        "Иван": "Петр",
        "Алексей": "Петр",
        "Петр": "Сергей",
        "Мария": "Сергей",
        "Елена": "Иван",
        "Сергей": "Александр",
        "Ольга": "Александр"
    }
    
    # Найти отца данного имени
    отец = семья.get(имя)
    if not отец:
        return f"Информация о человеке с именем {имя} не найдена."
    
    # Найти деда через отца
    дед = семья.get(отец)
    
    if дед:
        return f"Отец {имя} - {отец}. Дед {имя} - {дед}."
    else:
        return f"Информация о деде для {имя} не найдена."

# Запрос имени у пользователя
имя_человека = input("Введите имя человека: ").strip()
print(кто_твой_папа_и_дед(имя_человека))
