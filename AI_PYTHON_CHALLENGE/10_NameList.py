# Name List: Store 5 names and print them with their lengths

def name_list():
    names = []  # empty list to store names

    # Get 5 names from the user
    for i in range(5):
        name = input(f"Enter name {i+1}: ").strip()
        names.append(name)

    print("\n--- Names and Their Lengths ---")
    for name in names:
        print(f"{name} → {len(name)} characters")

# Run the program
if __name__ == "__main__":
    name_list()
