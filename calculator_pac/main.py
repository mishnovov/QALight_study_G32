from calculator.operations import add, subtract, multiply, divide, modulus, exponentiation, floor_division

def main():
    print("Welcome to Smart Calculator!")

    while True:
        operation = input("Enter an operation (+, -, *, /, %, **, //) or 'q' to quit: ")
        
        if operation == 'q':
            print("Thank you for using the Calculator!")
            break

        if operation in ('+', '-', '*', '/', '%', '**', '//'):
            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
                if operation == '+':
                    result = add(x, y)
                elif operation == '-':
                    result = subtract(x, y)
                elif operation == '*':
                    result = multiply(x, y)
                elif operation == '/':
                    result = divide(x, y)
                elif operation == '%':
                    result = modulus(x, y)
                elif operation == '**':
                    result = exponentiation(x, y)
                elif operation == '//':
                    result = floor_division(x, y)
                
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Invalid operation. Please enter a valid operation.")

if __name__ == "__main__":
    main()
