#У вас є файл із такими реченнями: Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. Where's the peck of pickled peppers Peter Piper picked.
#Потрібно вставити нове речення (If Peter Piper picked a peck of pickled peppers) після другого речення  в той самий рядок. 
#Бажаний результат: Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers. Where's the peck of pickled peppers Peter Piper picked.
#Тому найкраща практика:
#Прочитати речення з файлу,
#Внести необхідні зміни,
#Записати його в новий файл. 
#Використовуйте метод splitlines(), який повертає список рядків, розбитих на межі рядків.

def insert_sentence(filename, new_sentence):
    try:
        with open(filename, 'r') as file:
            lines = file.read().splitlines()

        # Перевіряємо, чи є хоча б два речення для вставки
        if len(lines) >= 2:
            lines.insert(2, new_sentence)
        else:
            print("Файл має недостатньо речень для вставки нового речення.")

        new_output_filename = r'D:\pyproj\Unit6_P57_Peter_OUT.txt' 

        with open(new_output_filename, 'w') as new_file:
            new_file.write('\n'.join(lines))

        print(f"Речення було вставлено у файл '{new_output_filename}'")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def main():
    input_filename = r'D:\pyproj\Unit6_P57_Peter_IN.txt'  
    new_sentence = "If Peter Piper picked a peck of pickled peppers."
    
    insert_sentence(input_filename, new_sentence)

if __name__ == "__main__":
    main()








