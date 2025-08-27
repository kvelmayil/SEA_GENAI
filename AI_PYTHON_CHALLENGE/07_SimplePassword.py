# Simple Password Checker

def check_password():
    MIN_LENGTH = 8  # Minimum password length

    password = input("Enter your password: ")

    if len(password) >= MIN_LENGTH:
        print("✅ Password accepted! Meets the minimum length requirement.")
    else:
        print(f"❌ Password too short! It must be at least {MIN_LENGTH} characters long.")

# Run the program
if __name__ == "__main__":
    check_password()
