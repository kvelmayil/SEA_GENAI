import time

# Countdown Timer from 10 to 0
def countdown_timer():
    print("⏳ Countdown starting...\n")
    for i in range(10, -1, -1):  # from 10 down to 0
        print(i)
        time.sleep(1)  # wait for 1 second
    print("\n🚀 Time's up!")

# Run the program
if __name__ == "__main__":
    countdown_timer()
