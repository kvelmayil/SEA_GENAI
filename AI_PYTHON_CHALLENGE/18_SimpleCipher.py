# Simple Cipher: Shift each letter by 1 position in the alphabet

def simple_cipher():
    word = input("Enter a word: ").strip().lower()
    result = ""

    for char in word:
        if char.isalpha():  # only shift letters
            if char == 'z':  # wrap around
                result += 'a'
            else:
                result += chr(ord(char) + 1)
        else:
            result += char  # keep non-letters as is

    print(f"\nOriginal Word : {word}")
    print(f"Ciphered Word : {result}")

# Run the program
if __name__ == "__main__":
    simple_cipher()
