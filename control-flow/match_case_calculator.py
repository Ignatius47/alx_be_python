num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
        case '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case '/':
            if num2 == 0:
                result = num1 / num2
                print(f"The result is {result}")
            else:
                print("cannot divide by zero")
        case _:
            print("Invalid operation. Please choose (+, -, *, /).")
