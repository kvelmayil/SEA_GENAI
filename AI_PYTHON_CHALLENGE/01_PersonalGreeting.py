def personal_greeting():
    print("Welcome! Let's get to know you.")
    
    # Get user input
    name = input("What's your name? ").strip().title()
    age = input("How old are you? ").strip()
    color = input("What's your favorite color? ").strip().capitalize()

    # Create personalized message
    print("\n--- Personalized Greeting ---")
    print(f"Hello {name}! You're {age} years young and {color} is such a vibrant color!")
    print("Have a colorful and amazing day!")

# Run the function
if __name__ == "__main__":
    personal_greeting()
