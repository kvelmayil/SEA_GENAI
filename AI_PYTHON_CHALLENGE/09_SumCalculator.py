# Sum Calculator: Find sum of numbers from 1 to n

def sum_calculator():
    try:
        n = int(input("Enter a positive integer n: "))

        if n < 1:
            print("Please enter a positive integer greater than 0.")
            return

        total = 0
        for i in range(1, n + 1):
            total += i

        print(f"The sum of numbers from 1 to {n} is: {total}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    sum_calculator()
