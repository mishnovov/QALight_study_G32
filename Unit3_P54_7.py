#Напишіть програму, щоб перевірити, порожній список чи ні.

#формуємо список
list_to_chek = input("Введіть значення: ")

# Перевіряємо, чи є список порожнім
if not list_to_chek:
    print("Список порожній.")
else:
    print("Список не є порожнім.")