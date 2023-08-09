#Напишіть функцію sum_by(lst, fn), що обчислює суму списку після зіставлення кожного елемента зі значенням за допомогою наданої функції lambda v : v['n'].

#- Використовуйте `map()` з `fn`, щоб зіставити кожен елемент із значенням за допомогою наданої функції.
#- Використовуйте `sum()`, щоб повернути суму значень.

#sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20

def sum_by(lst, fn):
    mapped_values = map(fn, lst)
    total = sum(mapped_values)
    return total

data = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
result = sum_by(data, lambda v: v['n'])
print(result) 
