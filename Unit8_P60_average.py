#Напишіть функцію average, що обчислює середнє значення двох чи більше чисел.

#- Використовуйте `sum()`, щоб підсумувати всі надані `args`

#average(*[1, 2, 3]) # 2.0
#average(1, 2, 3) # 2.0

def average(*args):
    total = sum(args)
    count = len(args)
    if count > 0:
        return total / count
    return 0  

result1 = average(*[1, 2, 3])
print(result1) 

result2 = average(1, 2, 3)
print(result2) 

