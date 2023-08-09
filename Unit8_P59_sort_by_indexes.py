#Напишіть функцію sort_by_indexes(a, b), що сортує один список на основі іншого списку, що містить потрібні індекси.
#- Використовуйте `zip()` і `sorted()`, щоб об’єднати та відсортувати два списки на основі значень `indexes`.
#- Використовуйте list comprehension, щоб отримати перший елемент кожної пари з результату.
#- Використовуйте параметр `reverse` в `sorted()`, щоб відсортувати словник у зворотному порядку на основі третього аргументу.

#a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
#b = [3, 2, 6, 4, 1, 5]
#sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
#sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']

def sort_by_indexes(a, indexes, reverse=False):
    sorted_pairs = sorted(zip(a, indexes), key=lambda pair: pair[1], reverse=reverse)
    sorted_a = [pair[0] for pair in sorted_pairs]
    return sorted_a

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

sorted_list = sort_by_indexes(a, b)
print(sorted_list) 

reverse_sorted_list = sort_by_indexes(a, b, True)
print(reverse_sorted_list) 
