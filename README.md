# Basic-Calculator-with-search-history
A very basic calculator is created which can perform simple arithmetic operations. It can also show the search history to the user. 

**Features:** 
This calculator has the following features:

Basic Arithmetic Operations: It supports the five core mathematical operations:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Modulus (Remainder, %)

Calculation History: It stores all successfully executed expressions and their results in an internal list.

View History Command: Users can enter the command h or history to retrieve and display the chronological list of all previous calculations.

Simple Input Handling: It processes simple, space-separated expressions consisting of two operands and one operator (e.g., 15 + 7.2).

Single Number Input: It can handle and store a single number as a valid "calculation" (e.g., typing 42 will be stored in history).

Zero Division Handling: It includes specific error handling to prevent the program from crashing when an attempted division by zero occurs.

User-Friendly Interface: It operates via a continuous command-line loop, providing a welcome message, instruction, and clear prompts for input.

Quit Command: Users can gracefully exit the program by entering q or quit.

Technologies/tools used:

Python (Core Language)

Standard Python Libraries:

operator Module: This built-in module is used to safely map the arithmetic symbols (+, -, *, /, %) to their corresponding Python functions (operator.add, operator.sub, etc.). This is a common practice for clean and safe expression evaluation.

Object-Oriented Programming (OOP): 

Standard Data Structures:

A Python List (self.history) is used.

A Python Dictionary (self.supported_operators) is used.

Command-Line Interface (CLI) Tools

Steps to install & run the project

1. Prerequisites (Python Installation)

2. Save the Code
   
3. Run the Calculator
   
4. Interact with the Calculator

Instructions for testing

Test 1: Basic Arithmetic Operations

Test Case	Input Expression	Expected Result	Expected History Entry

Export to Sheets

Steps:

Run the calculator.py script.

Enter each of the Input Expressions above one by one.

Verify that the output matches the Expected Result.

Test 2: Error and Edge Cases
Objective: Verify that the calculator handles invalid inputs and critical arithmetic errors gracefully without crashing.

Test Case	Input Expression	Expected Output	Expected History Change
Division by Zero	10 / 0	Error: Cannot divide by zero.	None (History should remain unchanged)
Invalid Operator	5 ^ 2	Error: Invalid input. Please enter a valid arithmetic expression...	None
Non-numeric Input	hello world	Error: Invalid input. Please enter a valid arithmetic expression...	None
Missing Operand	9 *	Error: Invalid expression format...	None

Export to Sheets

Steps:

Start with a clear history (or run a successful calculation first).

Enter each of the Input Expressions above.

Verify that the error message displayed matches the Expected Output.

Check the history (using the h command) to confirm that no error case was stored.

Test 3: History Storage and Retrieval
Objective: Verify that successful calculations are correctly recorded and displayed.

Steps:

Run the calculator.py script.

Perform the following two successful calculations:

10 + 2

3.5 * 2

Enter the command history (or h).

Verification: The output under the "Calculation History" section should clearly display exactly these two entries in this order:

--- Calculation History ---
1. 10 + 2 = 12.0
2. 3.5 * 2 = 7.0
---------------------------
Perform a third calculation:

40 - 1

Enter the command history again.

Verification: The output should now show three entries, with 40 - 1 = 39.0 added as the third item.

Test 4: Exit Functionality
Objective: Verify that the program terminates correctly.

Steps:

Run the calculator.py script.

Enter the command q or quit.

Verification: The program should immediately print the message "Thank you for using the calculator. Goodbye!" and stop running, returning you to the command line prompt.
