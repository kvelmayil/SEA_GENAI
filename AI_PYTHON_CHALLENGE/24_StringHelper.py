# String Helper Functions (improved)

def capitalize_sentence(text):
    # Sentence case: first letter uppercase, rest unchanged except leading/trailing spaces trimmed
    t = text.strip()
    return t[:1].upper() + t[1:] if t else t

def title_case(text):
    # Each word capitalized
    return text.strip().title()

def upper_case(text):
    # All caps
    return text.strip().upper()

def reverse_text(text):
    return text[::-1]

def count_characters(text):
    return len(text)

def string_helper():
    text = input("Enter a string: ")

    print("\n--- String Helper Functions ---")
    print(f"Original     : {text}")
    print(f"Sentence case: {capitalize_sentence(text)}")
    print(f"Title Case   : {title_case(text)}")
    print(f"ALL CAPS     : {upper_case(text)}")
    print(f"Reversed     : {reverse_text(text)}")
    print(f"Characters   : {count_characters(text)}")

if __name__ == "__main__":
    string_helper()
