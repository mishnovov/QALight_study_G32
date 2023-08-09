#Напишіть функцію compose(*fns), що виконує композицію функцій справа наліво.

#- Використовуйте `functools.reduce()` для композиції функції справа наліво.
#- Остання (крайня права) функція може приймати один або більше аргументів; решта функцій мають бути унарними.

#add5 = lambda x: x + 5
#multiply = lambda x, y: x * y
#multiply_and_add_5 = compose(add5, multiply)
#multiply_and_add_5(5, 2) # 15

import functools

def compose(*fns):
    return functools.reduce(lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs)), fns)

add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)

result = multiply_and_add_5(5, 2)
print(result)  






