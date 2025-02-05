import



def sum_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    s = s.lower().replace(" ", "")  # Normalize string
    return s == s[::-1]

def factorial(n):
    """Returns the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(n):
    """Returns True if a number is even, False otherwise."""
    return n % 2 == 0
