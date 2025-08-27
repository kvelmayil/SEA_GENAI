# Name Formatter: Display full name in different formats

def name_formatter():
    full_name = input("Enter your full name (First Middle Last): ").strip()

    # Split into parts
    parts = full_name.split()

    if len(parts) < 2:
        print("Please enter at least first and last name.")
        return

    first = parts[0]
    last = parts[-1]
    middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""

    print("\n--- Name Formats ---")
    print(f"Full Name       : {full_name}")
    print(f"First Last      : {first} {last}")
    print(f"Last, First     : {last}, {first}")
    if middle:
        print(f"First Middle Last : {first} {middle} {last}")
    print(f"Initials        : {''.join([p[0].upper() for p in parts])}")

# Run the program
if __name__ == "__main__":
    name_formatter()
