# Text Statistics: Count words, sentences, and characters in a paragraph

def text_statistics():
    paragraph = input("Enter a paragraph: ").strip()

    # Count characters (excluding spaces if needed)
    char_count = len(paragraph)

    # Count words (split by spaces)
    words = paragraph.split()
    word_count = len(words)

    # Count sentences (basic split by '.', '!', '?')
    sentence_count = 0
    for char in paragraph:
        if char in ".!?":
            sentence_count += 1

    print("\n--- Text Statistics ---")
    print(f"Characters : {char_count}")
    print(f"Words      : {word_count}")
    print(f"Sentences  : {sentence_count}")

# Run the program
if __name__ == "__main__":
    text_statistics()
