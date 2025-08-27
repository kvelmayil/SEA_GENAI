# Function to process numbers from a file
def number_file_processor(filename):
    try:
        with open(filename, "r") as file:
            # Read all lines and convert to numbers
            numbers = [float(line.strip()) for line in file if line.strip().isdigit() or line.strip().replace('.', '', 1).isdigit()]
        
        if numbers:
            total = sum(numbers)
            average = total / len(numbers)
            print(f"File: {filename}")
            print(f"Numbers: {numbers}")
            print(f"Sum = {total}")
            print(f"Average = {average:.2f}")
        else:
            print("No valid numbers found in the file.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Main program
if __name__ == "__main__":
    filename = input("Enter file name (with .txt): ")
    number_file_processor(filename)
