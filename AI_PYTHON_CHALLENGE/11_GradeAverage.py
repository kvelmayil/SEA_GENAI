# Grade Average: Calculate average of 5 test scores and determine pass/fail

def grade_average():
    scores = []

    # Get 5 test scores from the user
    for i in range(5):
        try:
            score = float(input(f"Enter score {i+1}: "))
            scores.append(score)
        except ValueError:
            print("Invalid input! Please enter a number.")
            return

    # Calculate average
    average = sum(scores) / len(scores)

    # Determine Pass/Fail (let's assume 40 is the passing mark)
    if average >= 40:
        result = "Pass ✅"
    else:
        result = "Fail ❌"

    # Show results
    print("\n--- Grade Report ---")
    print(f"Scores: {scores}")
    print(f"Average Score: {average:.2f}")
    print(f"Result: {result}")

# Run the program
if __name__ == "__main__":
    grade_average()
