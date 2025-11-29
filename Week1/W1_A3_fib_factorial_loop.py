# Week 1 - Activity 3 (Part 1)
# Fibonacci (Loop Version) + Factorial (Loop Version)
# No external packages allowed.

# FUNCTION: Generate N-length Fibonacci series (loop)
def fibonacci_series(n):
    # First two values of the Fibonacci sequence
    a, b = 0, 1
    series = []

    # Loop N times to generate the sequence
    for i in range(n):
        series.append(a)     # Store current number
        a, b = b, a + b      # Update to next pair

    return series


# FUNCTION: Compute factorial of N using loop
def factorial(n):
    result = 1

    # Multiply result by every number from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result


# MAIN PROGRAM
print("=== Week 1 Activity 3: Fibonacci & Factorial ===")

# Ask the user for a number N
num = int(input("Enter a number (N): "))

# Call both functions
fib_result = fibonacci_series(num)
fact_result = factorial(num)

# Display results
print("\nFibonacci Series (Length", num, "):")
print(fib_result)

print("\nFactorial of", num, ":")
print(fact_result)
