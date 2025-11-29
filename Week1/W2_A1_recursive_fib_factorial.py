# Week 2 - Activity 1
# Recursive Fibonacci & Factorial
# This version removes ALL loops and uses pure recursion.
# Comments included to explain recursion, stack behaviour, push, and pop.


# -------------------------------------------
# FACTORIAL USING RECURSION
# -------------------------------------------
def factorial(n):
    """
    Recursively computes n! (factorial of n).
    Recursion rule:
        n! = n * (n-1)!
        Base case: 0! = 1

    How memory works:
    - Each recursive call is added to the call stack (PUSH)
    - When base case is reached, results return back (POP)
    """
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case



# -------------------------------------------
# FIBONACCI USING RECURSION
# -------------------------------------------
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.
    
    Recursion rule:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2)

    Memory (Stack):
    - Each call pushes a new frame onto the stack
    - Once it hits the base case (0 or 1), it starts returning and popping
    """
    if n <= 1:
        return n  # Base cases
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calls



# -------------------------------------------
# MAIN PROGRAM
# -------------------------------------------
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        result = factorial(num)
    elif choice == "2":
        num = int(input("Enter position (n): "))
        result = fibonacci(num)
    else:
        result = "Invalid selection"

    print("\nFinal result:", result)
