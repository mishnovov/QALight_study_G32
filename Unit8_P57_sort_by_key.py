#Напишіть функцію, що сортує даний словник за ключем.

#- Використовуйте `dict.items()`, щоб отримати список пар кортежів з `d` і відсортувати його за допомогою `sorted()`.
#- Використовуйте `dict()`, щоб перетворити відсортований список назад у словник.
#- Використовуйте параметр `reverse` в `sorted()`, щоб відсортувати словник у зворотному порядку на основі другого аргументу.

#d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
#sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
#sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}

#Оголошуємо функцію
def sort_dict_by_key(dic, reverse=False):

#Отримауємо список пар кортежів
    items_list = list(dic.items())

#Сортуємо список пар кортежів
    sorted_items = sorted(dic.items(), key=lambda item: item[0], reverse=reverse)

#Перетворюємо відсортований список назад у словник
    sorted_dict = dict(sorted_items)
    return sorted_dict

dic = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}

#Сортуємо по ключам 
sorted_dic = sort_dict_by_key(dic)
print(sorted_dic)

#Сортуємо словник у зворотному порядку на основі другого аргументу
reverse_sorted_dic = sort_dict_by_key(dic, True)
print(reverse_sorted_dic)