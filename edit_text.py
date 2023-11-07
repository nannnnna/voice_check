import re

# Открываем файл для чтения и записи
with open('NLP_101.txt', 'r+', encoding='utf-8') as file:
    # Считываем все строки в список
    lines = file.readlines()
    # Переменная для отслеживания изменений
    modified = False
    # Очищаем файл
    file.seek(0)
    file.truncate()

    # Регулярное выражение для определения слова
    word_pattern = r'\b\w+\b'
    ignore_words = ["ignored", "номер", "неправильно", "сигнал", "звук", "вне", "зоны", "действия", "сети", "недоступен", "заблокирован", "недоступен", "алло", "Человек"]
    # Перебираем строки и записываем обратно только те строки, которые не соответствуют условиям
    for line in lines:
        words = re.findall(word_pattern, line)
        if len(words) >= 4:
            if any(word in line for word in ignore_words) or line.count("алло") > 3 or line.count("Человек") > 3:
                continue  # Пропустить строки, которые соответствуют другим условиям
            file.write(line)
        else:
            modified = True  # Если удалили строку, устанавливаем флаг изменений

    # Если были изменения, то записываем их на диск
    if modified:
        file.truncate()
