#Є файл sales.txt, який містить щомісячні дані про продажі товарів. Знайти у файлі рядок про продаж певного товару, надрукувати цей рядок та його номер. 
#Відкрити файл у режимі читання. 
#Використовуйте метод readlines(), щоб отримати всі рядки з файлу у формі об’єкта списку.
#Використовуйте цикл для повторення кожного рядка з файлу.
#В кожній ітерації циклу використовуйте умову if, щоб перевірити, чи присутній рядок у поточному рядку, і, якщо присутній, виведіть поточний рядок разом із номером рядка.

def find_product_sale(product_name):
    try:
        with open('D:/pyproj/Sales.txt', 'r') as file:
            lines = file.readlines()

            found = False
            for line_number, line in enumerate(lines, 1):
                if product_name in line:
                    print(f"Знайдено рядок у файлі 'Sales.txt', рядок номер {line_number}: {line.strip()}")
                    found = True

            if not found:
                print(f"Товар з назвою '{product_name}' не знайдено у файлі 'Sales.txt'")
    except FileNotFoundError:
        print("Файл 'Sales.txt' не знайдено")
        
def main():
    product_name = input("Введіть назву продукту (Product N): ")
    find_product_sale(product_name)

if __name__ == "__main__":
    main()
