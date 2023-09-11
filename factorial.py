def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input a number from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
print("Factorial of", num, "is", factorial_recursive(num))
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input a number from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
print("Factorial of", num, "is", factorial_recursive(num))
