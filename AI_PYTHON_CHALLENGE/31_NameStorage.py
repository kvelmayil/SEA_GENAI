# Function to save names to a file
def save_names(filename):
    count = int(input("How many names do you want to save? "))
    with open(filename, "w") as file:
        for i in range(count):
            name = input(f"Enter name {i+1}: ")
            file.write(name + "\n")
    print(f"✅ {count} names saved to {filename}")


# Function to read names from a file
def read_names(filename):
    try:
        with open(filename, "r") as file:
            names = file.readlines()
            print("\nNames stored in file:")
            for name in names:
                print(name.strip())
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")


# Main program
if __name__ == "__main__":
    filename = "names.txt"
    save_names(filename)
    read_names(filename)
