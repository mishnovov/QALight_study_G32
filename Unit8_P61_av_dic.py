#Є список словників [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }]
#Напишіть функцію, що обчислює середнє значення списку після зіставлення кожного елемента зі значенням за допомогою наданої функції lambda x: x['n'].

#- Використовуйте `map()`, щоб зіставити кожен елемент зі значенням, яке повертає `fn`.
#- Використовуйте `sum()`, щоб підсумувати всі зіставлені значення, розділити на `len(lst)`.
#- Пропустіть останній аргумент, `fn`, щоб використовувати функцію ідентифікації за замовчуванням.

def average_mapped(lst, fn=lambda x: x['n']):
    mapped_values = map(fn, lst)
    total = sum(mapped_values)
    count = len(lst)
    if count > 0:
        return total / count
    return 0  # Або можна повернути None

data = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
result = average_mapped(data)
print(result)  # 5.0

