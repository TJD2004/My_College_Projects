import os

from basic_operations import add, subtract, multiply, divide


LOG_FILE = 'logs/calculator_log.txt'

def log_operation(operation, result):
    """Logs the operation and result to a file."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'a') as file:
        file.write(f"{operation}: {result}\n")
print()

def main():
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))
            if choice in [1, 2, 3, 4]:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                if choice == 1:
                    result = add(a, b)
                    operation = f"{a} + {b}"

                elif choice == 2:
                    result = subtract(a, b)
                    operation = f"{a} - {b}"

                elif choice == 3:
                    result = multiply(a, b)
                    operation = f"{a} * {b}"

                elif choice == 4:
                    result = divide(a, b)
                    operation = f"{a} / {b}"

                print(f"Result: {result}")
                log_operation(operation, result)

            elif choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            else:
                print("Invalid choice! Please choose between 1-5.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()