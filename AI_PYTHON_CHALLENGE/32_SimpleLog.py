from datetime import datetime

# Function to write activity to log file
def write_log(filename, activity):
    with open(filename, "a") as file:  # "a" means append mode
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {activity}\n")
    print("✅ Activity logged successfully!")


# Function to read log file
def read_log(filename):
    try:
        with open(filename, "r") as file:
            print("\n📖 Activity Log:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"❌ Log file '{filename}' not found.")


# Main program
if __name__ == "__main__":
    filename = "daily_log.txt"
    
    while True:
        print("\n--- Daily Activity Logger ---")
        print("1. Write new activity")
        print("2. View log")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            activity = input("Enter your activity: ")
            write_log(filename, activity)
        elif choice == "2":
            read_log(filename)
        elif choice == "3":
            print("👋 Exiting logger. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
