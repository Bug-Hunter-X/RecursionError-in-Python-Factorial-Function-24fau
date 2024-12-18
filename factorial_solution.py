def factorial(n):
    if n < 0:
        return None  # Handle negative input
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(-1)) # This will now return None instead of raising an error