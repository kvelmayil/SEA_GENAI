# Find the largest number in a list without using max()

def find_maximum():
    try:
        # Take list input from user
        user_input = input("Enter numbers separated by commas: ")
        numbers = [float(n.strip()) for n in user_input.split(",")]

        # Assume first number is the largest
        largest = numbers[0]

        # Compare each number
        for num in numbers:
            if num > largest:
                largest = num

        print(f"\nThe largest number in the list is: {largest}")

    except ValueError:
        print("Invalid input! Please enter valid numbers separated by commas.")
    except IndexError:
        print("List is empty! Please enter at least one number.")

# Run the program
if __name__ == "__main__":
    find_maximum()
