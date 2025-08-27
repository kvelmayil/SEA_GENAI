# Vowel Counter: Count vowels in a word

def vowel_counter():
    word = input("Enter a word: ").strip().lower()  # lowercase for consistency
    vowels = "aeiou"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    print(f"\nThe word '{word}' contains {count} vowel(s).")

# Run the program
if __name__ == "__main__":
    vowel_counter()
