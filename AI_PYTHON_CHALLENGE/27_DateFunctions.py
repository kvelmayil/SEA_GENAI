from datetime import date

# Function to check leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to calculate age
def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

# Main program
def date_functions():
    # Leap year check
    year = int(input("Enter a year to check if it's a leap year: "))
    if is_leap_year(year):
        print(f"{year} is a Leap Year ✅")
    else:
        print(f"{year} is NOT a Leap Year ❌")

    # Age calculation
    birth_year = int(input("\nEnter your birth year: "))
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")

# Run the program
if __name__ == "__main__":
    date_functions()
