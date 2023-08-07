#Модуль pathlib має функцію read_text(), що читає текстовий файл 
#path.read_text().count("\n") читає текстовий файл і обчислює кількість рядків шляхом підрахунку рядків.
#len(path.read_text().split()) читає текстовий файл і обчислює кількість слів
#len(path.read_text()) читає текстовий файл і обчислює кількість символів, знаходячи довжину рядка.

#Написати скрипт, що може читати один або декілька текстових файлів і повідомляти, скільки рядків, слів і символів містить кожен із файлів.

from pathlib import Path

def analyze_text_file(file_path):
    try:
        path = Path(file_path)
        lines_count = path.read_text().count("\n")
        words_count = len(path.read_text().split())
        chars_count = len(path.read_text())
        
        print(f"Аналіз файлу '{file_path}':")
        print(f"Кількість рядків: {lines_count}")
        print(f"Кількість слів: {words_count}")
        print(f"Кількість символів: {chars_count}")
        print("=" * 30)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено")

def main():
    file_paths = [
        r'D:\pyproj\Unit6_P57_Peter_IN.txt',  # шлях до першого текстового файлу
        r'D:\pyproj\Unit6_P57_Peter_OUT.txt',  # шлях до другого текстового файлу
    ]
    
    for file_path in file_paths:
        analyze_text_file(file_path)

if __name__ == "__main__":
    main()
