# Определение пути к файлам
path_file1 = r"C:\Users\79819\Documents\GitHub\voice_check\NLP_demo_data_101.txt"
path_file2 = r"C:\Users\79819\Documents\GitHub\voice_check\text_from_excel.txt"

# Чтение данных из первого файла и сохранение их в список
with open(path_file1, 'r', encoding='utf-8') as f1:
    data1 = [line.strip().split('\t')[1] for line in f1]

# Чтение данных из второго файла
with open(path_file2, 'r', encoding='utf-8') as f2:
    data2 = f2.readlines()

# Проверка каждой строки из второго файла на наличие ее в первом
new_data = [line.strip() for line in data2 if line.strip() not in data1]

# Если есть новые данные, дописываем их в первый файл
if new_data:
    with open(path_file1, 'a', encoding='utf-8') as f1:
        for line in new_data:
            f1.write(f"1\t{line}\n")
