import emoji

def main():
    # Prompt user for text
    text = input("Input: ")
    # Convert emoji codes to actual emojis
    output = emoji.emojize(text, language="alias")
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
