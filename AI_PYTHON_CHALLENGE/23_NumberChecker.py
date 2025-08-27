# Function to check if number is positive
def is_positive(num):
    return num > 0

# Function to check if number is even
def is_even(num):
    return num % 2 == 0

# Function to check if number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Main program
def number_checker():
    try:
        num = int(input("Enter a number: "))

        print("\n--- Number Properties ---")
        print(f"Positive? : {'Yes' if is_positive(num) else 'No'}")
        print(f"Even?     : {'Yes' if is_even(num) else 'No'}")
        print(f"Prime?    : {'Yes' if is_prime(num) else 'No'}")

    except ValueError:
        print("Invalid input! Please enter an integer.")

# Run the program
if __name__ == "__main__":
    number_checker()
