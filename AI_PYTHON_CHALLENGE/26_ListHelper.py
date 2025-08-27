# Function to find maximum in a list
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Function to find minimum in a list
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Function to find sum of list
def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Function to find average
def find_average(numbers):
    return find_sum(numbers) / len(numbers) if numbers else 0


# Main program
def list_helper():
    numbers = [12, 7, 19, 3, 25, 8]

    print("List:", numbers)
    print("Maximum :", find_max(numbers))
    print("Minimum :", find_min(numbers))
    print("Sum     :", find_sum(numbers))
    print("Average :", find_average(numbers))

# Run the program
if __name__ == "__main__":
    list_helper()
