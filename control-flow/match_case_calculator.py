def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    operation = input("Choose the operation (+, -, *, /): ")
    
    match operation:
        case '+':
            # Addition
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            # Subtraction
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            # Multiplication
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            # Division
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                # Handle division by zero
                print("Cannot divide by zero.")
        case _:
            # Handle invalid operation input
            print("Invalid operation. Please choose from (+, -, *, /).")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
