#Написати скрипт виводу квадрата заданого числа
#Використовуючи модуль argparse, додати до скрипта підказку
#при виклику програми: python prog.py --help

#потрібно отримати такий результат:

#usage: square.py [-h] [-v] square

#positional arguments:
#  square         display a square of a given number

#options:
#  -h, --help     show this help message and exit
#  -v, --verbose  increase output verbosity

import argparse

def calculate_square(number):
    return number ** 2

def main():
    parser = argparse.ArgumentParser(description='Display a square of a given number')
    parser.add_argument('square', type=int, help='the number to be squared')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')

    args = parser.parse_args()

    result = calculate_square(args.square)

    if args.verbose:
        print(f"The square of {args.square} is {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()

