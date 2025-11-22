# Basic-Calculator-with-search-history

**Overview of the project:**
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

**Standard Python Libraries:**

operator Module: This built-in module is used to safely map the arithmetic symbols (+, -, *, /, %) to their corresponding Python functions (operator.add, operator.sub, etc.). This is a common practice for clean and safe expression evaluation.

Object-Oriented Programming (OOP): 

Standard Data Structures:

A Python List (self.history) is used.

A Python Dictionary (self.supported_operators) is used.

Command-Line Interface (CLI) Tools

**Steps to install & run the project:**

1. Prerequisites (Python Installation)

2. Save the Code
   
3. Run the Calculator
   
4. Interact with the Calculator

**Instructions for testing:**

Test 1: Basic Arithmetic Operations

Steps:

Run the calculator.
Enter each of the Input Expressions above one by one.
Verify that the output matches the Expected Result.

Test 2: Error and Edge Cases

Steps:

Start with a clear history (or run a successful calculation first).

Enter each of the Input Expressions above.
Verify that the error message displayed matches the Expected Output.
Check the history (using the h command) to confirm that no error case was stored.

Test 3: History Storage and Retrieval

Steps:

Run the calculator.
Perform successful calculations:
Enter the command history (or h).

Verification: The output under the "Calculation History" section should clearly display exactly same calculations in the same order:

Test 4: Exit Functionality

Steps:

Run the calculator.
Enter the command q or quit.
Verification: The program should immediately print the message "Thank you for using the calculator. Goodbye!" and stop running, returning you to the command line prompt.

**Screenshots of the output:**
<img width="1171" height="655" alt="image" src="https://github.com/user-attachments/assets/d6492825-c376-4eee-8deb-90ef91f84cc7" />
