# Initial Extractor: Extract initials from a full name

def initial_extractor():
    full_name = input("Enter your full name: ").strip()

    # Split name into parts and take first character of each
    initials = "".join([part[0].upper() for part in full_name.split() if part])

    print(f"\nFull Name : {full_name}")
    print(f"Initials  : {initials}")

# Run the program
if __name__ == "__main__":
    initial_extractor()
