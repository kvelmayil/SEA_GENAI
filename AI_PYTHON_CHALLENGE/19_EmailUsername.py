# Email Username Extractor

def email_username():
    email = input("Enter your email address: ").strip()

    if "@" in email:
        username = email.split("@")[0]
        print(f"\nEmail Address : {email}")
        print(f"Username      : {username}")
    else:
        print("Invalid email! Please include '@' in the address.")

# Run the program
if __name__ == "__main__":
    email_username()
