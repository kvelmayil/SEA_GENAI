# Function to convert feet to meters
def feet_to_meters(feet):
    return feet * 0.3048

# Function to convert meters to feet
def meters_to_feet(meters):
    return meters / 0.3048

# Function to convert pounds to kilograms
def pounds_to_kg(pounds):
    return pounds * 0.453592

# Function to convert kilograms to pounds
def kg_to_pounds(kg):
    return kg / 0.453592


# Main program
def conversion_functions():
    print("---- Unit Conversion ----")

    feet = float(input("Enter length in feet: "))
    print(f"{feet} feet = {feet_to_meters(feet):.2f} meters")

    pounds = float(input("\nEnter weight in pounds: "))
    print(f"{pounds} pounds = {pounds_to_kg(pounds):.2f} kilograms")


# Run the program
if __name__ == "__main__":
    conversion_functions()
