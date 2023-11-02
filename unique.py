# Путь к вашему файлу
path = r"C:\Users\79819\Documents\GitHub\voice_check\NLP_demo_data_101.txt"

# Чтение данных из файла и удаление дубликатов
with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    unique_lines = list(set(lines))

# Запись уникальных строк обратно в файл
with open(path, 'w', encoding='utf-8') as file:
    for line in unique_lines:
        file.write(line)

print("Дубликаты строк были удалены.")
