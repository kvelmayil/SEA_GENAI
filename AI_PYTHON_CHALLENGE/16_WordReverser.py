# Word Reverser: Reverse individual words in a sentence

def word_reverser():
    sentence = input("Enter a sentence: ").strip()

    # Split sentence into words, reverse each, then join back
    reversed_words = [word[::-1] for word in sentence.split()]
    result = " ".join(reversed_words)

    print(f"\nOriginal Sentence: {sentence}")
    print(f"Reversed Words   : {result}")

# Run the program
if __name__ == "__main__":
    word_reverser()
