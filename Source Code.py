import operator

class Calculator:
    """
    A simple command-line calculator that stores a history of calculations.
    """
    def __init__(self):
        # The history list stores tuples of (expression, result).
        self.history = []
        # Define supported operators for safe evaluation
        self.supported_operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod
        }

    def evaluate_expression(self, expression):
        """
        Evaluates a simple arithmetic expression (e.g., '5 + 3').
        For simplicity, this handles two operands and one operator.
        For more complex parsing, a proper math library is recommended.
        """
        try:
            # Normalize the expression by removing spaces
            expression = expression.strip()
            
            # Look for the operator in the expression
            op_symbol = None
            parts = None

            for symbol in self.supported_operators:
                if symbol in expression:
                    op_symbol = symbol
                    parts = expression.split(symbol)
                    break

            if not op_symbol:
                # If no supported operator is found, attempt direct conversion (e.g., just a number)
                try:
                    result = float(expression)
                    self.add_to_history(expression, result)
                    return f"Result: {result}"
                except ValueError:
                    return "Error: Invalid input. Please enter a valid arithmetic expression or number."
            
            if len(parts) != 2:
                return "Error: Invalid expression format. Use 'operand1 operator operand2' (e.g., '10 * 5')."

            # Extract and convert operands
            operand1 = float(parts[0])
            operand2 = float(parts[1])
            
            # Get the operation function
            operation = self.supported_operators[op_symbol]
            
            # Perform calculation
            if op_symbol == '/' and operand2 == 0:
                raise ZeroDivisionError

            result = operation(operand1, operand2)
            
            # Store the result in history
            self.add_to_history(expression, result)
            
            return f"Result: {result}"
            
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except ValueError:
            return "Error: Invalid number format in the expression."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def add_to_history(self, expression, result):
        """
        Adds a successful calculation to the history.
        """
        self.history.append((expression, result))

    def display_history(self):
        """
        Displays all recorded calculations.
        """
        if not self.history:
            print("\nHistory is empty. Perform some calculations first.")
            return

        print("\n--- Calculation History ---")
        for i, (expression, result) in enumerate(self.history, 1):
            # Format to show the calculation and its result
            print(f"{i}. {expression.strip()} = {result}")
        print("---------------------------\n")

def main():
    """
    The main function to run the interactive calculator program.
    """
    calc = Calculator()
    print("Welcome to the Python History Calculator!")
    print("Enter 'h' or 'history' to view the past calculations.")
    print("Enter 'q' or 'quit' to exit the calculator.")
    print("Supported operations: +, -, *, /, %")
    print("Example: 10 * 5 or 15 + 7.2")

    while True:
        try:
            user_input = input("\nEnter calculation or command: ").strip().lower()

            if user_input in ('q', 'quit'):
                print("Thank you for using the calculator. Goodbye!")
                break
            elif user_input in ('h', 'history'):
                calc.display_history()
            elif user_input:
                # Evaluate the expression
                output = calc.evaluate_expression(user_input)
                print(output)
            else:
                # Empty input, just continue
                continue

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nThank you for using the calculator. Goodbye!")
            break
        except Exception as e:
            print(f"A fatal error occurred: {e}")
            break

if __name__ == "__main__":
    main()
