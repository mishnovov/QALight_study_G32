def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("Ділення на нуль неможливе")

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def floor_division(x, y):
    return x // y
