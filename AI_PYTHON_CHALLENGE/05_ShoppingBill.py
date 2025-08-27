# Calculate total cost of 3 items including tax

def calculate_total():
    try:
        # Get item prices
        item1 = float(input("Enter price of Item 1: "))
        item2 = float(input("Enter price of Item 2: "))
        item3 = float(input("Enter price of Item 3: "))

        # Get tax percentage
        tax_rate = float(input("Enter tax percentage (%): "))

        # Subtotal before tax
        subtotal = item1 + item2 + item3

        # Tax amount
        tax_amount = subtotal * (tax_rate / 100)

        # Final total
        total = subtotal + tax_amount

        # Display results
        print("\n--- Bill Summary ---")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Tax ({tax_rate}%): {tax_amount:.2f}")
        print(f"Total Amount: {total:.2f}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Run the program
if __name__ == "__main__":
    calculate_total()
