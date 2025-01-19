# Simple Calculator Project

## Overview
This project is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. It also logs all operations to a file for record-keeping.

---

## Features
1. **Basic Arithmetic Operations**:
   - Addition
   - Subtraction
   - Multiplication
   - Division

2. **Logging**:
   - Each calculation is logged to a text file (`logs/calculator_log.txt`).

3. **Error Handling**:
   - Handles invalid inputs gracefully.
   - Prevents division by zero.

---

## Project Structure
. ├── arithmetic.py # Contains arithmetic functions (add, subtract, multiply, divide) ├── main.py # Main script to run the calculator ├── logs/ # Directory for log files │ └── calculator_log.txt # Log file for operations


---

## Requirements
- Python 3.6+

---

## How to Run
1. Clone or download the project to your local machine.
2. Ensure Python is installed.
3. Run the following command in the terminal:

   ```bash
   python main.py
Follow the on-screen instructions to perform calculations.

Example Usage
1. Starting the Program

Welcome to the Simple Calculator!

Options:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an option (1-5):

2. Performing an Operation
Input two numbers when prompted.
View the result.

Example:
Enter the first number: 5
Enter the second number: 3
Result: 8

3. Logging Example
After each operation, the result is logged to logs/calculator_log.txt.

Log entry example:

5 + 3: 8
Error Handling
Invalid Input: Handles non-numeric input gracefully.

Example:

Error: could not convert string to float: 'abc'
Division by Zero: Prevents invalid division operations.

Example:

Error: Cannot divide by zero.
Future Improvements
Add support for advanced operations (e.g., exponentiation, square root).
Build a graphical user interface (GUI).
Add unit tests for the arithmetic functions.
# License
This project is open-source and available under the MIT License.

---
