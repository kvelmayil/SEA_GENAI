# Phone Number Formatter

def phone_formatter():
    phone = input("Enter a 10-digit phone number: ").strip()

    # Remove any non-digit characters
    digits = "".join([c for c in phone if c.isdigit()])

    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print(f"\nFormatted Phone Number: {formatted}")
    else:
        print("Invalid input! Please enter exactly 10 digits.")

# Run the program
if __name__ == "__main__":
    phone_formatter()
