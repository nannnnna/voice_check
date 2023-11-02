# Путь к вашему файлу
path = r"C:\Users\79819\Documents\GitHub\voice_check\NLP_demo_data_101.txt"

# Чтение данных из файла
with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Отбор строк, которые не содержат "(ignored)"
filtered_lines = [line for line in lines if "(ignored)" not in line]

# Запись отфильтрованных строк обратно в файл
with open(path, 'w', encoding='utf-8') as file:
    for line in filtered_lines:
        file.write(line)

print("Строки, содержащие '(ignored)', были удалены.")
