#Напишіть програму для перевірки, чи є введене число простим


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True

# Зчитуємо число з консолі
num = int(input("Введіть число: "))

# Викликаємо функцію для перевірки
if is_prime(num):
    print(num, "просте число")
else:
    print(num, "не просте число")
