import os
import zipfile
import rarfile
import pandas as pd

# путь к UnRAR.exe
rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


# Извлекает все zip и rar архивы в указанном каталоге.
def extract_archives(input_dir):
    input_path = os.path.abspath(input_dir)  

    for file in os.listdir(input_path):  
        if not (file.lower().endswith('.zip') or file.lower().endswith('.rar')):
            continue  

        filepath = os.path.join(input_path, file)  
        if zipfile.is_zipfile(filepath):  
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(input_path)  
            print(f"Извлечён архив: {file}") 
        elif file.lower().endswith('.rar'):  
            with rarfile.RarFile(filepath, 'r') as rar_ref:
                rar_ref.extractall(input_path)  
            print(f"Извлечён архив: {file}")  


# Собирает данные из всех Excel и CSV файлов в каталоге и подкаталогах.
def collect_data(input_dir):
    input_path = os.path.abspath(input_dir)  
    dataframes = []  
    for file in os.listdir(input_path): 
        filepath = os.path.join(input_path, file)  
        if file.lower().endswith('.xlsx') or file.lower().endswith('.xls'):  # Проверка, является ли файл Excel
            try:
                df = pd.read_excel(filepath)  
                dataframes.append(df)  
                print(f"Загружен Excel файл: {file}")  
            except Exception as e:
                print(f"Ошибка при чтении {file}: {e}") 
        elif file.lower().endswith('.csv'):  
            try:
                df = pd.read_csv(filepath) 
                dataframes.append(df)  
                print(f"Загружен CSV файл: {file}")  
            except Exception as e:
                print(f"Ошибка при чтении {file}: {e}") 
    return dataframes 


def main(input_dir, output_file):
    # 1. Разархивирую архивы
    extract_archives(input_dir)
    # 2. Собираю все данные
    dataframes = collect_data(input_dir)
    if not dataframes:
        print("Не найдено ни одного подходящего файла для объединения!")
        return
    # 3. Объединяю в один DataFrame
    merged_df = pd.concat(dataframes, ignore_index=True)
    # 4. Сохраняю итоговый файл
    output_path = os.path.join(os.path.abspath(input_dir), output_file)
    merged_df.to_excel(output_path, index=False)
    print(f"Итоговый файл сохранён: {output_path}")


if __name__ == "__main__":
    input_dir = "."                 
    output_file = "merged_sales.xlsx"
    main(input_dir, output_file)
