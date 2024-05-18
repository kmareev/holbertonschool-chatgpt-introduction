#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Function Description:
        Computes the factorial of a given non-negative integer n.
        The factorial of n (n!) is the product of all positive integers
        up to n. The factorial of 0 is 1.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Check for valid command-line argument
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError
    except (IndexError, ValueError):
        print("Usage: python3 script_name.py <non-negative integer>")
        sys.exit(1)

    # Calculate and print factorial
    print(factorial(num))
