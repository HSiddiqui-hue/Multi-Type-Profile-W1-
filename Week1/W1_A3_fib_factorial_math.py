# Week 1 - Activity 3 (Part 2)
# Python math module simplifies factorial using math.factorial(), while the fibonacci
# series still requires the a custom function 

import math     # Importing math package for factorial()

# ----------------------------------------
# Fibonacci Function
# ----------------------------------------
# Generates the Fibonacci series up to N elements.
# This uses a simple loop because the goal of Part 2 is to show built-in usage,
# not to rewrite Fibonacci fully.
def fibonacci(n):
    series = []          # List to store Fibonacci numbers
    first = 0
    second = 1

    for _ in range(n):
        series.append(first)
        next_value = first + second
        first = second
        second = next_value

    return series


# ----------------------------------------
# Factorial using math.factorial()
# ----------------------------------------
# math.factorial(n) directly computes n! using optimized C-level code.
def factorial(n):
    return math.factorial(n)


# ----------------------------------------
# MAIN PROGRAM
# ----------------------------------------
print("Choose an option:")
print("1. Generate Fibonacci Series")
print("2. Calculate Factorial using math module")

choice = input("Enter choice (1/2): ")

if choice == "1":
    n = int(input("Enter the length of Fibonacci series: "))
    result = fibonacci(n)

elif choice == "2":
    n = int(input("Enter a number to find the factorial: "))
    result = factorial(n)

else:
    result = "Invalid choice"

print("\nFinal Result:", result)
