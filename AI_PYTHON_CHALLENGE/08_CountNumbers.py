# Count Positive, Negative, and Zero Numbers in a List

def count_numbers():
    try:
        # Input list from user
        user_input = input("Enter numbers separated by commas (e.g., -3, 0, 5, 7, -1): ")
        numbers = [int(n.strip()) for n in user_input.split(",")]

        # Initialize counters
        positive_count = 0
        negative_count = 0
        zero_count = 0

        # Count each number
        for num in numbers:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1
            else:
                zero_count += 1

        # Display result
        print("\n--- Count Results ---")
        print(f"Positive numbers: {positive_count}")
        print(f"Negative numbers: {negative_count}")
        print(f"Zeros: {zero_count}")

    except ValueError:
        print("Invalid input! Please enter only integers separated by commas.")

# Run the program
if __name__ == "__main__":
    count_numbers()
