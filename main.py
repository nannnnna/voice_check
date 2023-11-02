# Открываем файл с данными
with open(r"C:\Users\79819\Documents\GitHub\voice_check\NLP_demo_data_101.txt", "r", encoding="utf-8") as file:
    # Читаем файл построчно и создаем список из строк
    nlp_data = file.readlines()

# Удаляем пробельные символы и берем только текст из файла (без цифры в начале)
nlp_data_cleaned = [line.strip().split("\t")[1] for line in nlp_data]

# Открываем файл для проверки
with open(r"C:\Users\79819\Documents\GitHub\voice_check\output.txt", "r", encoding="utf-8") as file:
    # Читаем файл построчно и создаем список из строк
    voice_data = file.readlines()

# Убираем ненужные символы
voice_data_cleaned = [line.replace('"', '').strip() for line in voice_data]

# Проверяем каждую строку из voice_data_cleaned
for line in voice_data_cleaned:
    if line not in nlp_data_cleaned:
        # Если строки нет в nlp_data_cleaned, добавляем ее в nlp_data
        nlp_data.append("1\t" + line + "\n")

# Записываем обновленные данные обратно в файл
with open(r"C:\Users\79819\Documents\GitHub\voice_check\NLP_demo_data_101.txt", "w", encoding="utf-8") as file:
    file.writelines(nlp_data)
