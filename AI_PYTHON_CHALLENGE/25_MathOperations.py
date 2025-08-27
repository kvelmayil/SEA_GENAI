import math

# Function to calculate factorial
def factorial_num(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to calculate power (base^exp)
def power_num(base, exp):
    return base ** exp

# Function to calculate square root
def sqrt_num(n):
    if n < 0:
        return "Square root not defined for negative numbers"
    return math.sqrt(n)


# Main program
def math_operations():
    try:
        num = int(input("Enter a number: "))

        print("\n--- Math Operations ---")
        print(f"Factorial of {num}   : {factorial_num(num)}")
        print(f"{num} raised to 3    : {power_num(num, 3)}")
        print(f"Square root of {num} : {sqrt_num(num)}")

    except ValueError:
        print("Invalid input! Please enter an integer.")

# Run the program
if __name__ == "__main__":
    math_operations()
