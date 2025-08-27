# Number Comparison Script

def compare_numbers():
    try:
        # Get two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Compare numbers
        if num1 > num2:
            print(f"{num1} is larger than {num2}.")
        elif num1 < num2:
            print(f"{num1} is smaller than {num2}.")
        else:
            print(f"{num1} and {num2} are equal.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Run the program
if __name__ == "__main__":
    compare_numbers()
