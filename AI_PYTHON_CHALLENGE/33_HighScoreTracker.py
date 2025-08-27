import os

FILENAME = "high_scores.txt"

# Save a new score
def save_score(name, score):
    with open(FILENAME, "a") as file:
        file.write(f"{name},{score}\n")
    print("✅ Score saved successfully!")


# Load all scores
def load_scores():
    scores = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                scores.append((name, int(score)))
    return scores


# Show high score
def show_high_score():
    scores = load_scores()
    if scores:
        high_score = max(scores, key=lambda x: x[1])
        print(f"🏆 High Score: {high_score[0]} with {high_score[1]}")
    else:
        print("❌ No scores available yet.")


# Show all scores
def show_all_scores():
    scores = load_scores()
    if scores:
        print("\n📖 All Scores:")
        for name, score in scores:
            print(f"{name}: {score}")
    else:
        print("❌ No scores recorded yet.")


# Main program
if __name__ == "__main__":
    while True:
        print("\n--- High Score Tracker ---")
        print("1. Add new score")
        print("2. Show high score")
        print("3. Show all scores")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter player name: ")
            score = int(input("Enter score: "))
            save_score(name, score)
        elif choice == "2":
            show_high_score()
        elif choice == "3":
            show_all_scores()
        elif choice == "4":
            print("👋 Exiting High Score Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
