# Age Category Checker

def age_category():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif age <= 12:
            print("You are a Child.")
        elif age <= 19:
            print("You are a Teenager.")
        elif age <= 59:
            print("You are an Adult.")
        else:
            print("You are a Senior.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    age_category()
