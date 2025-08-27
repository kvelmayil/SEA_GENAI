# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Single number check
def single_number_check():
    try:
        num = int(input("Enter a number to check if it's Even or Odd: "))
        result = check_even_odd(num)
        print(f"{num} is {result}.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# List of numbers check
def list_number_check():
    try:
        input_list = input("Enter numbers separated by commas (e.g., 10, 25, 33): ")
        numbers = [int(n.strip()) for n in input_list.split(',')]

        print("\nEven or Odd results:")
        for num in numbers:
            result = check_even_odd(num)
            print(f"{num} → {result}")
    except ValueError:
        print("Invalid input! Please enter only integers separated by commas.")

# Run the program
if __name__ == "__main__":
    print("=== Even or Odd Checker ===")
    single_number_check()
    print("\nNow let's check a list of numbers.")
    list_number_check()
