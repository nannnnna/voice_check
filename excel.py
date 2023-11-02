import pandas as pd

# Путь к вашему файлу Excel
path_excel = r"C:\Users\79819\Documents\GitHub\voice_check\excell.xlsx"
# Путь к выходному текстовому файлу
path_txt = r"C:\Users\79819\Documents\GitHub\voice_check\output.txt"

# Загрузка данных из файла Excel
df = pd.read_excel(path_excel)


# Определение столбцов для обработки
cols = [col for col in df.columns if 'клиент' in str(col) or 'человек' in str(col)]


# Обработка данных: склеиваем текст из ячеек, игнорируя пустые ячейки
result_lines = []
for _, row in df.iterrows():
    line = " ".join([str(row[col]) for col in cols if pd.notna(row[col])])
    result_lines.append(line)

# Запись данных в текстовый файл
with open(path_txt, 'w', encoding='utf-8') as f:
    for line in result_lines:
        f.write(line + '\n')
