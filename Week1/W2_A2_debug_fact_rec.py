"""
Week 2 - Activity 4: Debugging factorial & fibonacci

Bug in original code:
- factorial() and fibonacci() were called with NO argument in main,
  but both functions require an 'n' parameter.
- This caused: TypeError: missing 1 required positional argument: 'n'

This fixed version:
- Asks the user for an integer n
- Validates the input
- Passes n correctly into factorial(n) or fibonacci(n)
"""

def factorial(n):
    """Recursive factorial function.

    Base case:
        if n == 0 → return 1
    Recursive case:
        n! = n * (n-1)!
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Recursive Fibonacci function.

    Base cases:
        if n == 0 → return 0
        if n == 1 → return 1
    Recursive case:
        F(n) = F(n-1) + F(n-2)
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
    # As calls reach base cases, results pop back up and combine.


if __name__ == "__main__":
    print("=== Week 2 - Activity 4: Debugging factorial & fibonacci ===")
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

11    choice = input("Enter choice (1/2): ").strip()

    # Ask the user for n only if they chose a valid option
    if choice in ("1", "2"):
        try:
            # Get n from the user
            n = int(input("Enter a non-negative integer (n): "))

            if n < 0:
                # Factorial and standard fibonacci are not defined for negative integers
                raise ValueError("n must be non-negative")

        except ValueError as e:
            # This block runs if the user types something that can't be converted to int
            print("Invalid input:", e)
            ans = None
        else:
            # Only run this part if there was NO error above
            if choice == "1":
                # BUG FIX: pass n into factorial(n)
                ans = factorial(n)
                print(f"\nFactorial of {n} (using recursion) is: {ans}")
            else:
                # BUG FIX: pass n into fibonacci(n)
                ans = fibonacci(n)
                print(f"\nFibonacci number at position {n} (using recursion) is: {ans}")
    else:
        ans = None
        print("Invalid choice")

    print("\nProgram finished.")