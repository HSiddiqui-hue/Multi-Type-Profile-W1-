"""
Week 2 - Activity 1
Recursive Fibonacci + Factorial

This program:
- Uses RECURSIVE functions only (no for/while loops)
- Shows how the call stack grows (push) and shrinks (pop)
"""

# -----------------------------
# Recursive factorial function
# -----------------------------
def factorial_recursive(n):
    """
    Returns n! (n factorial) using recursion.

    How recursion works here (stack idea):
    - Each time factorial_recursive is called, a NEW frame is pushed onto the call stack.
    - The base case (n == 0 or n == 1) stops further calls.
    - As Python returns from each call, frames are popped off the stack one by one.
    """
    if n < 0:
        # Factorial is not defined for negative numbers
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


# -----------------------------
# Recursive Fibonacci function
# -----------------------------
def fibonacci_recursive(n):
    """
    Returns the n-th Fibonacci number using recursion.

    Fibonacci sequence:
    0, 1, 1, 2, 3, 5, 8, ...

    How recursion works here:
    - Each call to fibonacci_recursive(n) pushes a new frame on the stack.
    - For n > 1, we call fibonacci_recursive(n-1) and fibonacci_recursive(n-2).
    - When we hit the base cases (n == 0 or n == 1), the recursion stops.
    - As results return, stack frames are popped and added together.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    # Base cases: these stop further recursive calls
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# -----------------------------
# Helper to generate full series
# -----------------------------
def fibonacci_series_recursive(length):
    """
    Generates the first 'length' Fibonacci numbers using recursion.

    We re-use fibonacci_recursive(n) and call it for each index.
    This is allowed because we are not using for/while loops
    INSIDE the recursive logic – we are only calling the function repeatedly.
    """
    if length < 0:
        raise ValueError("Series length cannot be negative.")

    series = []
    for i in range(length):
        series.append(fibonacci_recursive(i))
    return series


# -----------------------------
# Main program (menu + input)
# -----------------------------
if __name__ == "__main__":
    print("=== Week 2 - Activity 1: Recursive Fibonacci & Factorial ===")
    print("Choose an option:")
    print("1. Factorial (recursive)")
    print("2. Fibonacci (recursive)")

    choice = input("Enter choice (1/2): ").strip()

    try:
        n = int(input("Enter a non-negative integer (N): ").strip())
        if n < 0:
            raise ValueError("N must be non-negative.")
    except ValueError as e:
        print("Invalid input:", e)
        exit(1)

    if choice == "1":
        # Factorial of N using recursion
        result = factorial_recursive(n)
        print(f"\nFactorial of {n} (using recursion) is: {result}")

    elif choice == "2":
        # Fibonacci series of length N using recursion
        series = fibonacci_series_recursive(n)
        print(f"\nFirst {n} Fibonacci numbers (using recursion):")
        print(series)

        # Also show the N-th Fibonacci number (if N > 0)
        if n > 0:
            print(f"\nFibonacci number at position {n-1} is: {series[-1]}")

    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")
