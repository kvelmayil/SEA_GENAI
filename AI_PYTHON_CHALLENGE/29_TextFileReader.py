# Function to read file and count lines & words
def text_file_reader(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

        print(f"File: {filename}")
        print(f"Total Lines: {line_count}")
        print(f"Total Words: {word_count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Main program
if __name__ == "__main__":
    filename = input("Enter file name (with .txt): ")
    text_file_reader(filename)
